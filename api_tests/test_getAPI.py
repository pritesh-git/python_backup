import requests
import pytest

user_url = "https://reqres.in/api/users"  # Default User URL
resource_url = "https://reqres.in/api/unknown"  # Default Resource URL
urlParam = {"page": 1}  # Default Param for url


@pytest.mark.users
def test_user_list():
    resp = requests.get(user_url, urlParam)  # Multi User List Fetch API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"
    assert resp.cookies is not None, "No Cookie Passed In Response"

    user_list = resp.json()  # Convert to JSON for accessing data easily.

    assert user_list["total"] >= 1, "Total Number Of Data Is Less"
    assert user_list["total_pages"] >= 1, "Total Number Of Pages Is Less"
    assert type(user_list["data"][0]["id"]) is int, "Id Should Not Be Number"
    assert user_list["data"][0]["first_name"] is not None, "FirstName Should Not Be Null"
    assert user_list["data"][0]["last_name"] is not None, "LastName Should Not Be Null"
    assert user_list["data"][0]["email"].endswith("reqres.in"), "Email Format Not Valid"
    assert user_list["data"][0]["avatar"].endswith(".jpg"), "Image Not In Supported Format"


# -----------------------------------------------------

@pytest.mark.users
def test_single_user():
    resp = requests.get(user_url + '/2')  # Single User Fetch API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"
    assert resp.cookies != '', "No Cookie Passed In Response"

    user = resp.json()  # Convert to JSON for accessing data easily.

    assert user["data"]["first_name"] is not None, "FirstName Should Not Be Null"
    assert user["data"]["last_name"] is not None, "LastName Should Not Be Null"
    assert user["data"]["email"].endswith("reqres.in"), "Email Format Not Valid"
    assert user["data"]["avatar"].endswith(".jpg"), "Image Not In Supported Format"


# -----------------------------------------------------

@pytest.mark.users
def test_wrong_user():
    resp = requests.get(user_url + '/50')  # Wrong User Fetch API,This Should Fail
    assert resp.status_code == 404, "Status Code Should Be 404"


# ==========================================================

@pytest.mark.resource
def test_resource_list():
    resp = requests.get(resource_url)  # Multi Resource List Fetch API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"
    assert resp.cookies is not None, "No Cookie Passed In Response"

    resp_list = resp.json()  # Convert to JSON for accessing data easily.

    assert resp_list["total"] >= 1, "Total Number Of Data Is Less"
    assert resp_list["total_pages"] >= 1, "Total Number Of Pages Is Less"
    assert resp_list["data"][0]["name"] is not None, "Name Should Not Be Null"
    assert resp_list["data"][0]["year"] is not None, "Year Should Not Be Null"
    assert type(resp_list["data"][0]["year"]) is int, "Year Should Not Be Number"
    assert resp_list["data"][0]["color"].startswith("#"), "Color Code Should Be Valid"
    assert resp_list["data"][0]["pantone_value"] is not None, "Pantone Should Not Be Null"


# -----------------------------------------------------

@pytest.mark.resource
def test_single_resource():
    resp = requests.get(resource_url + '/2')  # Single Resource Fetch API
    assert resp.status_code == 200, "API Failed,Status Should Be 200"
    assert resp.cookies is not None, "No Cookie Passed In Response"

    resp_list = resp.json()  # Convert to JSON for accessing data easily.

    assert resp_list["data"]["name"] is not None, "Name Should Not Be Null"
    assert resp_list["data"]["year"] is not None, "Year Should Not Be Null"
    assert type(resp_list["data"]["year"]) is int, "Year Should Not Be Number"
    assert resp_list["data"]["color"].startswith("#"), "Color Code Should Be Valid"
    assert resp_list["data"]["pantone_value"] is not None, "Pantone Should Not Be Null"


# -----------------------------------------------------

@pytest.mark.resource
def test_wrong_resource():
    resp = requests.get(resource_url + '/50')  # Wrong Resource Fetch API,This Should Fail
    assert resp.status_code == 404, "Status Code Should Be 404"
