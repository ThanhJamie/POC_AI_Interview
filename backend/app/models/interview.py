from __future__ import annotations

from datetime import datetime, timezone
from typing import ClassVar
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Interview(SQLModel, table=True):
    __tablename__: ClassVar[str] = "interviews"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    candidate_name: str = Field(index=True, max_length=255)
    job_title: str | None = Field(default=None, max_length=255)
    status: str = Field(default="created", max_length=50)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
