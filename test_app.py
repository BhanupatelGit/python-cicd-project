from app import app


def test_home_status():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_content():
    client = app.test_client()
    response = client.get("/")
    assert b"Hello CI/CD" in response.data


def test_invalid_route():
    client = app.test_client()
    response = client.get("/invalid")
    assert response.status_code == 404
