import os

os.environ["DATABASE_URL"] = "sqlite:///./test_contract.db"
os.environ["REDIS_URL"] = "redis://localhost:6379/0"

from fastapi.testclient import TestClient

from app.main import app


def test_create_interview_smoke() -> None:
    payload = {"candidate_name": "Nguyen Van A", "job_title": "Backend Engineer"}
    with TestClient(app) as client:
        response = client.post("/interviews", json=payload)
        assert response.status_code in (200, 201)
        body = response.json()
        assert "id" in body
        assert body["candidate_name"] == payload["candidate_name"]


def test_read_interview_not_found() -> None:
    with TestClient(app) as client:
        response = client.get("/interviews/00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404
