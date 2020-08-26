from services.http.http_client import HttpClient
from utils.enums.endpoints import Endpoints
from configs import API_HOST


class UsersServiceHttpClient(HttpClient):

    def __init__(self, validate=False):
        super().__init__(API_HOST, validate)

    def get_user_by_Id(self, id=None):
        req = self.get()
        req.uri(Endpoints.users.value)
        if id is not None:
            req.query_params(**{"id": id})
        return req.send()

    def create_user(self, body=None):
        req = self.post()
        req.uri(Endpoints.users.value)
        req.body(body)
        return req.send()
