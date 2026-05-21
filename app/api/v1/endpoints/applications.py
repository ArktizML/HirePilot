from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.application import ApplicationCreate, ApplicationRead, ApplicationUpdate
from app.services.application_service import ApplicationService

router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("/job/{job_id}", response_model=list[ApplicationRead])
def get_all_by_job(job_id: int, db: Session = Depends(get_db)) -> list[ApplicationRead]:
    return ApplicationService(db).get_all_by_job(job_id)


@router.get("/{application_id}", response_model=ApplicationRead)
def get_application(application_id: int, db: Session = Depends(get_db)) -> ApplicationRead:
    return ApplicationService(db).get_by_id(application_id)


@router.post("/", response_model=ApplicationRead, status_code=status.HTTP_201_CREATED)
def create_application(data: ApplicationCreate, db: Session = Depends(get_db)) -> ApplicationRead:
    return ApplicationService(db).create(data)


@router.patch("/{application_id}", response_model=ApplicationRead)
def update_application(application_id: int, data: ApplicationUpdate, db: Session = Depends(get_db)) -> ApplicationRead:
    return ApplicationService(db).update(application_id, data)


@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: int, db: Session = Depends(get_db)) -> None:
    ApplicationService(db).delete(application_id)