from sqlalchemy.orm import Session

from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationUpdate


class ApplicationRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, application_id: int) -> Application | None:
        return self.db.get(Application, application_id)

    def get_all_by_job(self, job_id: int) -> list[Application]:
        return self.db.query(Application).filter(Application.job_id == job_id).all()

    def create(self, data: ApplicationCreate) -> Application:
        application = Application(**data.model_dump())
        self.db.add(application)
        self.db.commit()
        self.db.refresh(application)
        return application

    def update(self, application: Application, data: ApplicationUpdate) -> Application:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(application, field, value)
        self.db.commit()
        self.db.refresh(application)
        return application

    def delete(self, application: Application) -> None:
        self.db.delete(application)
        self.db.commit()