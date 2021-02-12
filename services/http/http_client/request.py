from urllib.parse import urljoin

from services.http.http_client.api_exc import ApiException
from services.http.http_client.response import Response
from utils.logger import log


class Request:
    """
    Class request builder
    :param method: requests HTTP method, requests.post, requests.get etc.
    :param base_uri: base URL for request
    :param: validate: if True - verify that response is OK automatically
    """

    def __init__(self, method, base_uri, validate=True):
        self._method = method
        self._base_uri = base_uri
        self._validate = validate
        self._uri = None
        self._body = None
        self._data = None
        self._headers = {}
        self._query_params = {}

    def uri(self, endpoint):
        """
        Set URI for request
        :param endpoint: request endpoint
        """
        self._uri = urljoin(self._base_uri, endpoint)

    def body(self, body):
        """
        Set request JSON body
        :param body: either Python JSON-serializable object or string
        """
        self._body = body

    def form_data(self, data):
        """
        Set form data
        :param data: dict
        """
        self._data = data

    def headers(self, **headers):
        """
        Add request headers. Each method call adds new headers
        """
        self._headers.update(headers)

    def query_params(self, **query_params):
        """Add request query params. Each method call adds new query params"""
        self._query_params.update(query_params)

    def send(self):
        """
        Send request
        :return: Response object
        """
        log.debug("{method}: {uri}".format(method=self._method.__name__.upper(), uri=self._uri))
        if self._query_params:
            log.debug("QUERY_PARAMS: {}".format(self._query_params))
        if self._body:
            log.debug("BODY: {}".format(self._body))
        if self._data:
            log.debug("FORM DATA: {}".format(self._data))

        res = self._method(self._uri, json=self._body, data=self._data, headers=self._headers,
                           params=self._query_params)
        if self._validate:
            self._is_response_ok(res)
        return Response(res)

    @staticmethod
    def _is_response_ok(res):
        """Check is response OK"""
        if not res.ok:
            raise ApiException(res)
