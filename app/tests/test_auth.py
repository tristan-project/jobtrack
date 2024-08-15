import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust if your app's entry point is different
import uuid


client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Initialize a test database connection and create a test user.
    client.post(
        "/auth/register",
        json={
            "email": "testuser@example.com",
            "password": "testpassword",
            "profile": {
                "username": "TestUser",
                "name": "Test User"
            }
        }
    )
    yield
    # Optional: Add cleanup logic here, if necessary

def test_register_user():
    unique_email = f"testuser_{uuid.uuid4()}@example.com"
    unique_username = f"testuser_{uuid.uuid4()}"
    print(unique_email + unique_username)
    response = client.post(
        "/auth/register",
        json={
            "email": unique_email,  # Ensure this email is unique
            "password": "testpassword",
            "profile": {
                "username": unique_username,
                "name": "User2",
            }
        }
    )
    print(response.json())  # Keep this for debugging if needed
    assert response.status_code == 200

def test_login_user():
    # Use a unique email for each test to avoid conflicts
    client.post(
        "/auth/register",
        json={
            "email": "testlogin2@example.com",
            "password": "testpassword",
            "profile": {
                "username": "TestLogin2",
                "name": "User2",
            }
        }
    )

    response = client.post(
        "/auth/login",
        json={
            "email": "testlogin2@example.com",
            "password": "testpassword"
        }
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_homepage_with_valid_token(setup_database):
    client.post(
        "/auth/register",
        json={
            "email": "testhomepage2@example.com",
            "password": "testpassword",
            "profile": {
                "username": "TestHomepage2",
                "name": "User2",
            }
        }
    )
    response = client.post(
        "/auth/login",
        json={
            "email": "testhomepage2@example.com",
            "password": "testpassword"
        }
    )
    print(response.json())  # Keep this for debugging
    access_token = response.json().get("access_token")
    assert access_token is not None

    response = client.get(
        "/auth/homepage",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("text/html")

def test_user_data_with_valid_token():
    client.post(
        "/auth/register",
        json={
            "email": "testuserdata2@example.com",
            "password": "testpassword",
            "profile": {
                "username": "TestUserData2",
                "name": "User2",
            }
        }
    )
    
    response = client.post(
        "/auth/login",
        json={
            "email": "testuserdata2@example.com",
            "password": "testpassword"
        }
    )
    access_token = response.json().get("access_token")

    response = client.get(
        "/auth/user-data",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == "testuserdata2@example.com"

def test_homepage_with_invalid_token():
    response = client.get(
        "/auth/homepage",
        headers={"Authorization": "Bearer invalid_token"}
    )
    assert response.status_code == 401

def test_user_data_without_token():
    response = client.get("/auth/user-data")
    assert response.status_code == 401
