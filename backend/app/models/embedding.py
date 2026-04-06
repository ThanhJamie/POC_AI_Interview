from __future__ import annotations

from datetime import datetime, timezone
from typing import ClassVar
from uuid import UUID, uuid4

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class Embedding(SQLModel, table=True):
    __tablename__: ClassVar[str] = "embeddings"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    interview_id: UUID | None = Field(
        default=None, foreign_key="interviews.id", index=True
    )
    source_type: str = Field(max_length=64)
    source_ref: str = Field(max_length=255)
    vector: list[float] = Field(sa_column=Column(JSON, nullable=False))
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
