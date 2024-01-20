import requests
import pytest

user_url = "https://reqres.in/api/users"  # Default User URL
user_details = {"name": "morpheus", "job": "zion resident"}

@pytest.mark.users
def test_put_request():
    resp = requests.put(user_url+'/2', data=user_details)  # Update User API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"

    user = resp.json()  # Convert to JSON for accessing data easily.

    assert user["name"] == user_details["name"], "Name Should Be Same"
    assert user["job"] == user_details["job"], "Job Should Be Same"
    assert user["updatedAt"] is not None, "Update Date/Time Should Not Be Null"


# -----------------------------------------------------

@pytest.mark.users
def test_patch_request():
    resp = requests.patch(user_url+'/2', data=user_details)  # Update User API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"

    user = resp.json()  # Convert to JSON for accessing data easily.

    assert user["name"] == user_details["name"], "Name Should Be Same"
    assert user["job"] == user_details["job"], "Job Should Be Same"
    assert user["updatedAt"] is not None, "Update Date/Time Should Not Be Null"


# -----------------------------------------------------

@pytest.mark.users
def test_delete_request():
    resp = requests.delete(user_url + '/2')  # Delete User API
    assert resp.status_code == 204, "API Failed,Status Should Be 204"

