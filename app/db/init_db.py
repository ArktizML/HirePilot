from app.db.base import Base
from app.db.session import engine
from app.models import application, job  # noqa: F401 - imports needed for Base to register models


def init_db() -> None:
    Base.metadata.create_all(bind=engine)