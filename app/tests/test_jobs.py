import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.deps import get_db
from app.db.base import Base
from app.main import app

TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


client = TestClient(app)


def test_get_all_jobs_empty():
    response = client.get("/api/v1/jobs/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_job():
    payload = {"title": "Python Developer", "company": "Google"}
    response = client.post("/api/v1/jobs/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Python Developer"
    assert data["company"] == "Google"
    assert "id" in data


def test_get_job_not_found():
    response = client.get("/api/v1/jobs/999")
    assert response.status_code == 404