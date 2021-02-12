import pytest
from services.http.rest_service.users_service import UsersServiceHttpClient
# from utils.sort import ordered # read below 
from test_data import USER_IDS


def test_create_user(user):
    users_http = UsersServiceHttpClient(validate=True)
    body = user.return_body()
    res = users_http.create_user(body)
    assert res.status == 201
    assert_response_contains_request_data(res, body)
    get_created_users_back(users_http, res.json)


def test_create_same_user(same_user, user):
    users_http = UsersServiceHttpClient(validate=False)
    body = user.return_body()
    res = users_http.create_user(body)
    assert res.status == 400
    assert res.body == '{"status":400,"message":"User already exists"}'


@pytest.mark.parametrize("ids", USER_IDS)
def test_get_user_by_id(ids):
    users_http = UsersServiceHttpClient(validate=True)
    res = users_http.get_user_by_Id(id=int(ids[0]))
    assert res.status == 200


def get_created_users_back(service, body):
    res = service.get_user_by_Id(id == body['id'])
    assert res.status == 200
    assert_response_contains_request_data(res, body)


def assert_response_contains_request_data(response, request):
    assert all(k in response.json and response.json[k] == v for k, v in request.items())
    # could be slightly different validation as well: assert ordered(response.json) == ordered(request)


# pipenv run pytest tests/api_backend
# pipenv run pytest tests/api_backend/test_users_api.py
