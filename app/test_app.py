import pytest
from app import app

@pytest.fixture
def client():
    # 1. Enable testing mode
    app.config['TESTING'] = True
    
    # 2. Disable CSRF only for the test environment
    # This prevents the 400 Bad Request error during automated tests
    app.config['WTF_CSRF_ENABLED'] = False 
    
    with app.test_client() as client:
        yield client

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