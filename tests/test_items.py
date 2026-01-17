from fastapi.testclient import TestClient

from main import app


def test_get_course_material():
    client = TestClient(app)
    response = client.get("/items/course")

    assert response.status_code == 200
    payload = response.json()
    assert "items" in payload
    assert isinstance(payload["items"], list)
    assert payload["items"][0]["id"] == "course"
    assert payload["items"][0]["items"][0]["id"] == "lab-01"
    assert payload["items"][0]["items"][1]["id"] == "lab-02"


def test_list_items():
    client = TestClient(app)
    response = client.get("/items")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert payload[0]["id"] == "course"


def test_get_item_by_id():
    client = TestClient(app)
    response = client.get("/items/lab-01")

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "lab-01"
    assert isinstance(payload.get("items"), list)
    assert payload["items"][0]["id"] == "lab-01-setup"
