from fastapi.testclient import TestClient

from main import app


def test_get_course_material():
    client = TestClient(app)
    response = client.get("/items/course")

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "software_engineering_toolkit"
    assert payload["type"] == "course"
    assert isinstance(payload.get("items"), list)
    assert payload["items"][0]["id"] == "lab-02"


def test_list_items():
    client = TestClient(app)
    response = client.get("/items")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert payload[0]["id"] == "software_engineering_toolkit"


def test_get_item_by_id():
    client = TestClient(app)
    response = client.get("/items/lab-02-run-local")

    assert response.status_code == 200
    payload = response.json()
    assert payload["id"] == "lab-02-run-local"
    assert payload["type"] == "task"
    assert isinstance(payload.get("items"), list)
    assert payload["items"][0]["type"] == "step"
