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


def test_parse_job(client: TestClient):
    job = client.post("/api/v1/jobs/", json={"title": "Python Dev", "company": "Google"}).json()
    response = client.post(f"/api/v1/jobs/{job['id']}/parse")
    assert response.status_code == 200
    data = response.json()
    assert "skills" in data
    assert "seniority" in data


def test_parse_job_saves_to_db(client: TestClient):
    job = client.post("/api/v1/jobs/", json={"title": "Python Dev", "company": "Google"}).json()
    client.post(f"/api/v1/jobs/{job['id']}/parse")
    updated = client.get(f"/api/v1/jobs/{job['id']}").json()
    assert updated["parsed_data"] is not None
    assert "skills" in updated["parsed_data"]