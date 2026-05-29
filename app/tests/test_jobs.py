from fastapi.testclient import TestClient


def test_get_all_jobs_empty(client: TestClient):
    response = client.get("/api/v1/jobs/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_job(client: TestClient):
    payload = {"title": "Python Developer", "company": "Google"}
    response = client.post("/api/v1/jobs/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Python Developer"
    assert data["company"] == "Google"
    assert "id" in data


def test_get_job_not_found(client: TestClient):
    response = client.get("/api/v1/jobs/999")
    assert response.status_code == 404