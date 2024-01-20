import requests
import pytest

user_url = "https://reqres.in/api/users"  # Default User URL
login_url = "https://reqres.in/api/login"  # Default Login URL
register_url = "https://reqres.in/api/register"  # Default Register URL
user_details = {"name": "Rajesh", "job": "Developer"}
signup_details = {"email": "eve.holt@reqres.in", "password": "123456"}


@pytest.mark.users
def test_create_user():
    resp = requests.post(user_url, data=user_details)  # Create User API
    assert resp.status_code == 201, "API Failed,Status Should Be 201"

    user = resp.json()  # Convert to JSON for accessing data easily.

    assert user["id"] is not None, "Id Should Not Be Null"
    assert user["name"] == user_details["name"], "Name Should Be Same"
    assert user["job"] == user_details["job"], "Job Should Be Same"
    assert user["createdAt"] is not None, "Create Date/Time Should Not Be Null"


# -----------------------------------------------------

@pytest.mark.register
def test_register_user():
    resp = requests.post(register_url, data=signup_details)  # Register User API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"

    user = resp.json()  # Convert to JSON for accessing data easily.

    assert user["id"] is not None, "Id Should Not Be Null"
    assert type(user["id"]) is int, "Id Should Not Be Number"
    assert user["token"] is not None, "Token Should Not Be Null"


# -----------------------------------------------------

@pytest.mark.register
def test_wrong_register():
    resp = requests.post(register_url, data={})  # Register Fail API
    assert resp.status_code == 400, "API Failed,Status Should Be 400"

    user = resp.json()  # Convert to JSON for accessing data easily.

    assert user["error"] is not None, "Error Should Not Be Null"
    assert user["error"] == 'Missing email or username', "Wrong Error message"


# -----------------------------------------------------

@pytest.mark.login
def test_login_user():
    resp = requests.post(login_url, data=signup_details)  # Login User API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"

    user = resp.json()  # Convert to JSON for accessing data easily.

    assert user["token"] is not None, "Token Should Not Be Null"
