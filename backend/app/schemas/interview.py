from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class InterviewCreate(BaseModel):
    candidate_name: str = Field(min_length=1, max_length=255)
    job_title: str | None = Field(default=None, max_length=255)


class InterviewRead(BaseModel):
    id: UUID
    candidate_name: str
    job_title: str | None
    status: str
    created_at: datetime
    updated_at: datetime


class InterviewList(BaseModel):
    items: list[InterviewRead]
