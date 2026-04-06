from __future__ import annotations

import inspect
from collections import defaultdict, deque
from datetime import datetime, timezone
from time import monotonic

from redis.asyncio import Redis

from app.models.ws_message import SessionState, WSInboundMessage, WSOutboundMessage


class RateLimitExceeded(Exception):
    pass


class UnsupportedMessageType(Exception):
    pass


class WebSocketSessionManager:
    def __init__(
        self,
        redis_url: str,
        *,
        rate_limit_max: int = 20,
        rate_limit_window_seconds: int = 60,
        session_ttl_seconds: int = 3600,
    ) -> None:
        self.redis_url = redis_url
        self.rate_limit_max = rate_limit_max
        self.rate_limit_window_seconds = rate_limit_window_seconds
        self.session_ttl_seconds = session_ttl_seconds

        self._redis: Redis | None = None
        self._redis_disabled = False
        self._memory_states: dict[str, SessionState] = {}
        self._rate_windows: defaultdict[str, deque[float]] = defaultdict(deque)

    def _key(self, session_id: str) -> str:
        return f"ws:interview:{session_id}"

    async def _get_redis(self) -> Redis | None:
        if self._redis_disabled:
            return None

        if self._redis is None:
            self._redis = Redis.from_url(self.redis_url, decode_responses=True)

        try:
            ping_result = self._redis.ping()
            if inspect.isawaitable(ping_result):
                await ping_result
            return self._redis
        except Exception:
            self._redis_disabled = True
            return None

    async def load_state(self, session_id: str) -> SessionState:
        redis = await self._get_redis()
        if redis is not None:
            raw = await redis.get(self._key(session_id))
            if raw:
                try:
                    state = SessionState.model_validate_json(raw)
                    self._memory_states[session_id] = state
                    return state
                except Exception:
                    pass

        if session_id in self._memory_states:
            return self._memory_states[session_id]

        state = SessionState(session_id=session_id)
        self._memory_states[session_id] = state
        return state

    async def save_state(self, state: SessionState) -> None:
        state.last_activity = datetime.now(timezone.utc)
        self._memory_states[state.session_id] = state

        redis = await self._get_redis()
        if redis is not None:
            await redis.set(self._key(state.session_id), state.model_dump_json())
            await redis.expire(self._key(state.session_id), self.session_ttl_seconds)

    async def register_connection(self, session_id: str) -> SessionState:
        state = await self.load_state(session_id)
        await self.save_state(state)
        return state

    def _enforce_rate_limit(self, session_id: str) -> None:
        now = monotonic()
        window = self._rate_windows[session_id]

        while window and now - window[0] > self.rate_limit_window_seconds:
            window.popleft()

        if len(window) >= self.rate_limit_max:
            raise RateLimitExceeded(f"Rate limit exceeded for session {session_id}")

        window.append(now)

    async def handle_message(
        self,
        session_id: str,
        message: WSInboundMessage,
    ) -> WSOutboundMessage:
        if message.type == "ping":
            return WSOutboundMessage(type="pong", payload={"session_id": session_id})

        self._enforce_rate_limit(session_id)
        state = await self.load_state(session_id)
        state.message_count += 1
        state.last_message_type = message.type

        if message.type == "audio_chunk":
            state.audio_chunk_count += 1
            payload = {
                "session_id": session_id,
                "message": "audio_chunk_received",
                "chunk_index": message.payload.get("chunk_index"),
                "duration_ms": message.payload.get("duration_ms"),
                "stored": "metadata_only",
            }
            out_type = "audio_chunk_ack"
        elif message.type == "transcript":
            state.transcript_count += 1
            payload = {
                "session_id": session_id,
                "message": "transcript_received",
                "segment_id": message.payload.get("segment_id"),
            }
            out_type = "transcript_ack"
        elif message.type == "assistant_response":
            state.assistant_response_count += 1
            payload = {
                "session_id": session_id,
                "message": "assistant_response_received",
                "response_id": message.payload.get("response_id"),
            }
            out_type = "assistant_response_ack"
        else:
            raise UnsupportedMessageType(f"Unsupported message type: {message.type}")

        await self.save_state(state)
        payload["state"] = state.model_dump(mode="json")
        return WSOutboundMessage(type=out_type, payload=payload)
