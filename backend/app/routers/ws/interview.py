from __future__ import annotations

import json

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, status
from pydantic import ValidationError

from app.config import settings
from app.models.ws_message import WSInboundMessage, WSOutboundMessage
from app.services.websocket_manager import (
    RateLimitExceeded,
    UnsupportedMessageType,
    WebSocketSessionManager,
)

router = APIRouter()
manager = WebSocketSessionManager(
    settings.redis_url,
    rate_limit_max=settings.ws_rate_limit_max,
    rate_limit_window_seconds=settings.ws_rate_limit_window_seconds,
    session_ttl_seconds=settings.ws_session_ttl_seconds,
)


@router.websocket("/ws/interview/{session_id}")
async def interview_websocket(websocket: WebSocket, session_id: str) -> None:
    await websocket.accept()

    state = await manager.register_connection(session_id)
    ack = WSOutboundMessage(
        type="connection_ack",
        payload={
            "session_id": session_id,
            "state": state.model_dump(mode="json"),
        },
    )
    await websocket.send_json(ack.model_dump(mode="json"))

    while True:
        try:
            raw_text = await websocket.receive_text()
        except WebSocketDisconnect:
            break

        try:
            data = json.loads(raw_text)
        except json.JSONDecodeError:
            err = WSOutboundMessage(
                type="error",
                payload={
                    "code": "invalid_json",
                    "message": "Message must be valid JSON",
                },
            )
            await websocket.send_json(err.model_dump(mode="json"))
            continue

        try:
            inbound = WSInboundMessage.model_validate(data)
            outbound = await manager.handle_message(session_id, inbound)
            await websocket.send_json(outbound.model_dump(mode="json"))
        except ValidationError as exc:
            err = WSOutboundMessage(
                type="error",
                payload={
                    "code": "invalid_message",
                    "message": "Message schema validation failed",
                    "detail": str(exc),
                },
            )
            await websocket.send_json(err.model_dump(mode="json"))
        except RateLimitExceeded as exc:
            err = WSOutboundMessage(
                type="error",
                payload={
                    "code": "rate_limited",
                    "message": str(exc),
                },
            )
            await websocket.send_json(err.model_dump(mode="json"))
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
            break
        except UnsupportedMessageType as exc:
            err = WSOutboundMessage(
                type="error",
                payload={
                    "code": "unsupported_type",
                    "message": str(exc),
                },
            )
            await websocket.send_json(err.model_dump(mode="json"))
