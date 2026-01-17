from fastapi.testclient import TestClient

from main import app


def test_get_outcomes():
    client = TestClient(app)
    response = client.get("/outcomes")

    assert response.status_code == 200
    payload = response.json()
    assert "outcomes" in payload
    assert payload["outcomes"][0]["id"] == "course-outcomes"


def test_get_outcome_by_id():
    client = TestClient(app)
    response = client.get("/outcomes/lab-02-outcome-deploy")

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "lab-02-outcome-deploy"

