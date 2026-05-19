from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.job import JobCreate, JobRead
from app.services.job_service import JobService

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/", response_model=list[JobRead])
def get_all_jobs(db: Session = Depends(get_db)) -> list[JobRead]:
    return JobService(db).get_all()


@router.get("/{job_id}", response_model=JobRead)
def get_job(job_id: int, db: Session = Depends(get_db)) -> JobRead:
    return JobService(db).get_by_id(job_id)


@router.post("/", response_model=JobRead, status_code=status.HTTP_201_CREATED)
def create_job(data: JobCreate, db: Session = Depends(get_db)) -> JobRead:
    return JobService(db).create(data)


@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, db: Session = Depends(get_db)) -> None:
    JobService(db).delete(job_id)