import uuid
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_user_and_profile():
    user_email = "testprofileuser@example.com"
    user_password = "testpassword"
    
    # Try to log in with the given credentials
    login_response = client.post(
        "/auth/login",
        json={"email": user_email, "password": user_password}
    )
    
    if login_response.status_code == 200:
        access_token = login_response.json().get("access_token")
        assert access_token
    else:
        # Register and log in to get the access token
        register_response = client.post(
            "/auth/register",
            json={
                "email": user_email,
                "password": user_password,
                "profile": {
                    "username": "ProfileUser",
                    "name": "Test Profile User"
                }
            }
        )
        assert register_response.status_code == 200
        login_response = client.post(
            "/auth/login",
            json={"email": user_email, "password": user_password}
        )
        access_token = login_response.json().get("access_token")
        assert access_token

    # Create a profile for the user
    profile_response = client.post(
        "/profile/",
        json={
            "profile": {
                "username": "ProfileUser",
                "name": "Test Profile User"
            }
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert profile_response.status_code == 200
    profile_data = profile_response.json()
    assert 'id' in profile_data

    yield {
        "access_token": access_token,
        "profile_id": profile_data["id"]
    }



def test_create_profile(setup_user_and_profile):
    access_token = setup_user_and_profile["access_token"]
    unique_username = f"testuser_{uuid.uuid4()}"
    response = client.post(
        "/profile/",
        json={
            "username": unique_username, 
            "name": "Test Name"
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    profile_data = response.json()
    assert 'id' in profile_data

def test_read_profile(setup_user_and_profile):
    access_token = setup_user_and_profile["access_token"]

    response = client.get(
        "/profile/",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    profile_data = response.json()
    assert 'name' in profile_data
    assert profile_data['name'] == "Test Profile User"


def test_patch_profile(setup_user_and_profile):
    access_token = setup_user_and_profile["access_token"]

    response = client.patch(
        "/profile/",
        json={
            "about": "Partially updated about."
        },
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    profile_data = response.json()
    assert profile_data['about'] == "Partially updated about."