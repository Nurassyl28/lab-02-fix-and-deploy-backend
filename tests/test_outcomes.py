from fastapi.testclient import TestClient
from main import app

def test_get_all_outcomes():
    client = TestClient(app)
    response = client.get("/outcomes")
    
    assert response.status_code == 200
    payload = response.json()
    assert "outcomes" in payload
    assert isinstance(payload["outcomes"], list)
    assert len(payload["outcomes"]) > 0
    assert payload["outcomes"][0]["id"] == "course-outcomes"

def test_get_outcome_by_id():
    client = TestClient(app)
    response = client.get("/outcomes/lab-02-outcome-local-dev")
    
    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "lab-02-outcome-local-dev"
    assert "suboutcomes" in payload
    assert isinstance(payload["suboutcomes"], list)

def test_get_outcome_not_found():
    client = TestClient(app)
    response = client.get("/outcomes/non-existent-outcome")
    
    assert response.status_code == 404
