import requests
from services.http.http_client.request import Request


class HttpClient:
    """
    Http Client provides access to requests objects
    :param validate_requests: validate that request is ok by default
    """

    def __init__(self, base_uri, validate_requests=False):
        self._base_uri = base_uri
        self._validate = validate_requests

    def _prepare_request(self, method):
        """
        Prepare request object with given method and pre-defined data
        :param method: requests HTTP method, requests.post, requests.get etc.
        :return: instance of Request
        """
        request_ = Request(method, base_uri=self._base_uri, validate=self._validate)
        return request_

    def post(self):
        """Return POST Request"""
        return self._prepare_request(requests.post)

    def get(self):
        """Return GET Request"""
        return self._prepare_request(requests.get)

    def patch(self):
        """Return PATCH Request"""
        return self._prepare_request(requests.patch)

    def put(self):
        """Return PUT request"""
        return self._prepare_request(requests.put)

    def delete(self):
        """Return DELETE request"""
        return self._prepare_request(requests.delete)
