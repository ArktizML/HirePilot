from fastapi.testclient import TestClient


def _create_job(client: TestClient) -> int:
    response = client.post("/api/v1/jobs/", json={"title": "Python Dev", "company": "Google"})
    return response.json()["id"]


def test_get_all_applications_empty(client: TestClient):
    job_id = _create_job(client)
    response = client.get(f"/api/v1/applications/job/{job_id}")
    assert response.status_code == 200
    assert response.json() == []


def test_create_application(client: TestClient):
    job_id = _create_job(client)
    response = client.post("/api/v1/applications/", json={"job_id": job_id})
    assert response.status_code == 201
    data = response.json()
    assert data["job_id"] == job_id
    assert data["status"] == "applied"
    assert "id" in data


def test_get_application_not_found(client: TestClient):
    response = client.get("/api/v1/applications/999")
    assert response.status_code == 404