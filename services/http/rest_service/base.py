from configs import REST_SERVICE_HOST
from services.http.http_client import HttpClient


class RestService(HttpClient):
    """Base class for REST service clients"""

    def __init__(self, validate=True, api_key=None):
        auth = None
        if api_key:
            auth = {"key": api_key}
        super().__init__(REST_SERVICE_HOST, validate, auth)
