from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate


class JobRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, job_id: int) -> Job | None:
        return self.db.get(Job, job_id)

    def get_all(self) -> list[Job]:
        return self.db.query(Job).all()

    def create(self, data: JobCreate) -> Job:
        job = Job(**data.model_dump())
        self.db.add(job)
        self.db.commit()
        self.db.refresh(job)
        return job

    def update(self, job: Job, data: JobUpdate) -> Job:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(job, field, value)
        self.db.commit()
        self.db.refresh(job)
        return job

    def delete(self, job: Job) -> None:
        self.db.delete(job)
        self.db.commit()