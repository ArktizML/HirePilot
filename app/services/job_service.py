from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError
from app.models.job import Job
from app.repositories.job_repository import JobRepository
from app.schemas.job import JobCreate, JobUpdate


class JobService:
    def __init__(self, db: Session) -> None:
        self.repository = JobRepository(db)

    def get_by_id(self, job_id: int) -> Job:
        job = self.repository.get_by_id(job_id)
        if job is None:
            raise NotFoundError(f"Job with id {job_id} not found")
        return job

    def get_all(self) -> list[Job]:
        return self.repository.get_all()

    def create(self, data: JobCreate) -> Job:
        return self.repository.create(data)

    def update(self, job_id: int, data: JobUpdate) -> Job:
        job = self.get_by_id(job_id)
        return self.repository.update(job, data)

    def delete(self, job_id: int) -> None:
        job = self.get_by_id(job_id)
        self.repository.delete(job)