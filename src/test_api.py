from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_first_foo():
    response = client.get("/first_test")
    assert response.status_code == 200

