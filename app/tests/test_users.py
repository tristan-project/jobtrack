import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_user_and_job():
    user_email = "testuser@example.com"
    user_password = "testpassword"
    
    # Try to log in with the given credentials
    login_response = client.post(
        "/auth/login",
        json={"email": user_email, "password": user_password}
    )
    
    if login_response.status_code == 200:
        # User exists, retrieve the access token
        access_token = login_response.json().get("access_token")
    else:
        # User does not exist, create a new one
        register_response = client.post(
            "/auth/register",
            json={
                "email": user_email,
                "password": user_password,
                "profile": {
                    "username": "TestUser",
                    "name": "Test User"
                }
            }
        )
        assert register_response.status_code == 200
        

    # Fetch user data using the access token
    response = client.get(
        "/auth/user-data",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data

    # Yield user data for the tests
    yield user_data

    # Clean up by deleting the user
    client.delete("/auth/delete", json={"email": user_email})

def test_read_users_me(setup_user_and_job):
    user = setup_user_and_job
    login_response = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testpassword"}
    )
    assert login_response.status_code == 200
    access_token = login_response.json().get("access_token")


    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data['email'] == user['email']


def test_user_data_with_token(setup_user_and_job):
    user = setup_user_and_job
    login_response = client.post(
        "/auth/login",
        json={"email": "testuser@example.com", "password": "testpassword"}
    )
    assert login_response.status_code == 200
    access_token = login_response.json().get("access_token")

    response = client.get(
        "/users/user-data",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    user_data = response.json()
    assert user_data['email'] == user['email']