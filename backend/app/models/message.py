from __future__ import annotations

from datetime import datetime, timezone
from typing import ClassVar
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Message(SQLModel, table=True):
    __tablename__: ClassVar[str] = "messages"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    interview_id: UUID = Field(foreign_key="interviews.id", index=True)
    role: str = Field(max_length=32)
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
