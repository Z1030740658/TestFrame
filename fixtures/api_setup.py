import pytest
from models.user_model import User
from services.http.users_service import UsersServiceHttpClient


@pytest.fixture(scope="session")
def user():
    """Create fake user object for POST"""
    return User()


@pytest.fixture(scope="session")
def same_user(user):
    """Returns JSON of created user object"""
    users_http = UsersServiceHttpClient(validate=True)
    body = user.return_body()
    res = users_http.create_user(body)
    return res.json
