from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError
from app.models.application import Application
from app.repositories.application_repository import ApplicationRepository
from app.schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationService:
    def __init__(self, db: Session) -> None:
        self.repository = ApplicationRepository(db)

    def get_by_id(self, application_id: int) -> Application:
        application = self.repository.get_by_id(application_id)
        if application is None:
            raise NotFoundError(f"Application with id {application_id} not found")
        return application

    def get_all_by_job(self, job_id: int) -> list[Application]:
        return self.repository.get_all_by_job(job_id)

    def create(self, data: ApplicationCreate) -> Application:
        return self.repository.create(data)

    def update(self, application_id: int, data: ApplicationUpdate) -> Application:
        application = self.get_by_id(application_id)
        return self.repository.update(application, data)

    def delete(self, application_id: int) -> None:
        application = self.get_by_id(application_id)
        self.repository.delete(application)