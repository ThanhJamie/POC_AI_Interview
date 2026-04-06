from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select

from app.database import get_session
from app.models.interview import Interview
from app.schemas.interview import InterviewCreate, InterviewList, InterviewRead

router = APIRouter(prefix="/interviews", tags=["interviews"])


@router.post("", response_model=InterviewRead, status_code=status.HTTP_201_CREATED)
def create_interview(
    payload: InterviewCreate,
    session: Session = Depends(get_session),
) -> Interview:
    interview = Interview(
        candidate_name=payload.candidate_name,
        job_title=payload.job_title,
    )
    session.add(interview)
    session.commit()
    session.refresh(interview)
    return interview


@router.get("/{interview_id}", response_model=InterviewRead)
def get_interview(
    interview_id: UUID,
    session: Session = Depends(get_session),
) -> Interview:
    interview = session.get(Interview, interview_id)
    if interview is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Interview not found"
        )
    return interview


@router.get("", response_model=InterviewList)
def list_interviews(
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    session: Session = Depends(get_session),
) -> InterviewList:
    statement = select(Interview).offset(offset).limit(limit)
    items = session.exec(statement).all()
    mapped_items = [InterviewRead.model_validate(item) for item in items]
    return InterviewList(items=mapped_items)
