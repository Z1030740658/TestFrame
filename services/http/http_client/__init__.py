import requests
from services.http.http_client.request import Request


class HttpClient:
    """
    Http Client provides access to requests objects
    :param validate_requests: validate that request is ok by default
    :param auth_headers: dict with headers that going to be added to every request by default -
    unless specified otherwise
    """

    def __init__(self, base_uri, validate_requests=True, auth_headers=None):
        self._base_uri = base_uri
        self._validate = validate_requests
        self._auth_headers = auth_headers

    def _prepare_request(self, method, auth):
        """
        Prepare request object with given method and pre-defined data
        :param method: requests HTTP method, requests.post, requests.get etc.
        :param auth: if True - add auth headers to request if they exist
        :return: instance of Request
        """
        request_ = Request(method, base_uri=self._base_uri, validate=self._validate)
        if auth and self._auth_headers:
            request_.headers(**self._auth_headers)
        return request_

    def post(self, auth=True):
        """Return POST Request"""
        return self._prepare_request(requests.post, auth)

    def get(self, auth=True):
        """Return GET Request"""
        return self._prepare_request(requests.get, auth)

    def patch(self, auth=True):
        """Return PATCH Request"""
        return self._prepare_request(requests.patch, auth)

    def put(self, auth=True):
        """Return PUT request"""
        return self._prepare_request(requests.put, auth)

    def delete(self, auth=True):
        """Return DELETE request"""
        return self._prepare_request(requests.delete, auth)
