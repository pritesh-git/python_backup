import pytest


@pytest.mark.smoke
def test_login():
    print("Login to application")


@pytest.mark.regression
def test_checkout():
    print("Checkout")


@pytest.mark.smoke
def test_logout():
    print("Logout from application")
