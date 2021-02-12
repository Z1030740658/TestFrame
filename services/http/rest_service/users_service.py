from services.http.rest_service.base import RestService
from utils.enums.endpoints import Endpoints


class UsersServiceHttpClient(RestService):

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
