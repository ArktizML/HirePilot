from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.job import JobRead
from app.services.job_service import JobService

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=list[JobRead])
def get_all_jobs(db: Session = Depends(get_db)) -> list[JobRead]:
    return JobService(db).get_all()


@router.get("/{job_id}", response_model=JobRead)
def get_job(job_id: int, db: Session = Depends(get_db)) -> JobRead:
    return JobService(db).get_by_id(job_id)