import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# Test home route
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello DevSecOps!" in response.data

# Test login success
def test_login_success(client):
    response = client.post("/login", data={
        "username": "admin",
        "password": "admin"
    })
    assert response.status_code == 200
    assert b"Logged in!" in response.data

# Test login failure
def test_login_fail(client):
    response = client.post("/login", data={
        "username": "user",
        "password": "wrong"
    })
    assert response.status_code == 200
    assert b"Invalid credentials" in response.data