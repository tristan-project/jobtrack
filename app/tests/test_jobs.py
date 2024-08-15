import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import get_db
from app.models.user import User
from app.models.job import Job

client = TestClient(app)


@pytest.fixture(scope="module")
def setup_user_and_job():
    user_email = "testjobuser@example.com"
    user_password = "testpassword"
    
    # Try to log in with the given credentials
    login_response = client.post(
        "/auth/login",
        json={"email": user_email, "password": user_password}
    )
    
    if login_response.status_code == 200:
        # User already exists
        access_token = login_response.json().get( "access_token")
    else:
        # User does not exist, create a new one
        register_response = client.post(
            "/auth/register",
            json={
                "email": user_email,
                "password": user_password,
                "profile": {
                    "username": "JobUser",
                    "name": "Test Job User"
                }
            }
        )
        access_token = register_response.json()
        assert register_response.status_code == 200


    response = client.get(
        "/auth/user-data",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    user_id = response.json()
    assert 'id' in user_id


    # Yield user data for the tests
    yield user_id



def test_create_job(setup_user_and_job):
    user = setup_user_and_job
    response = client.post(
        "/auth/login",
        json={
            "email": "testjobuser@example.com",
            "password": "testpassword"
        }
    )
    token = response.json().get("access_token")
    # user_id = response.json().get("id")
    # print(user_id)


    response = client.post(
        "/jobs/createjob",
        json={
            "title": "Test Job",
            "description": "Test Job Description",
            "owner_id": user["id"]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Job"


def test_read_job(setup_user_and_job):
    user = setup_user_and_job
    response = client.post(
        "/auth/login",
        json={
            "email": "testjobuser@example.com",
            "password": "testpassword"
        }
    )
    token = response.json().get("access_token")

    # First, create a job to read
    job_response = client.post(
        "/jobs/createjob",
        json={
            "title": "Job to Read",
            "description": "Description of job to read",
            "owner_id": user["id"]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    job_id = job_response.json()["id"]
    
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Job to Read"


def test_read_jobs(setup_user_and_job):
    user = setup_user_and_job
    response = client.post(
        "/auth/login",
        json={
            "email": "testjobuser@example.com",
            "password": "testpassword"
        }
    )
    token = response.json().get("access_token")

    # Create a couple of jobs to read in bulk
    client.post(
        "/jobs/createjob",
        json={
            "title": "Bulk Job 1",
            "description": "First bulk job",
            "owner_id": user["id"]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    client.post(
        "/jobs/createjob",
        json={
            "title": "Bulk Job 2",
            "description": "Second bulk job",
            "owner_id": user["id"]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert len(response.json()) >= 2


def test_update_job(setup_user_and_job):
    user = setup_user_and_job
    response = client.post(
        "/auth/login",
        json={
            "email": "testjobuser@example.com",
            "password": "testpassword"
        }
    )
    token = response.json().get("access_token")

    # First, create a job to update
    job_response = client.post(
        "/jobs/createjob",
        json={
            "title": "Job to Update",
            "description": "Description of job to update",
            "owner_id": user["id"]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    job_id = job_response.json()["id"]

    # Update the job
    response = client.put(
        f"/jobs/{job_id}",
        json={
            "title": "Updated Job Title",
            "description": "Updated Job Description"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Job Title"


def test_delete_job(setup_user_and_job):
    user = setup_user_and_job
    response = client.post(
        "/auth/login",
        json={
            "email": "testjobuser@example.com",
            "password": "testpassword"
        }
    )
    token = response.json().get("access_token")

    # First, create a job to delete
    job_response = client.post(
        "/jobs/createjob",
        json={
            "title": "Job to Delete",
            "description": "Description of job to delete",
            "owner_id": user["id"]
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    job_id = job_response.json()["id"]

    # Delete the job
    response = client.delete(
        f"/jobs/{job_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200

    # Ensure the job is deleted
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 404