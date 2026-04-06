from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal

from pydantic import BaseModel, Field

MessageType = Literal["audio_chunk", "transcript", "assistant_response", "ping"]


class WSInboundMessage(BaseModel):
    type: MessageType
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payload: dict[str, Any] = Field(default_factory=dict)


class WSOutboundMessage(BaseModel):
    type: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payload: dict[str, Any] = Field(default_factory=dict)


class SessionState(BaseModel):
    session_id: str
    message_count: int = 0
    audio_chunk_count: int = 0
    transcript_count: int = 0
    assistant_response_count: int = 0
    last_message_type: str | None = None
    last_activity: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
