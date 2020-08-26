import json


class Response:
    """
    Response wrapper
    """

    def __init__(self, response_obj):
        self._response = response_obj

    @property
    def json(self):
        """Return response body parsed JSON"""
        return self._response.json()

    @property
    def status(self):
        """Return response status code"""
        return self._response.status_code

    @property
    def body(self):
        """Return utf-8 encoded response body as text"""
        return str(self._response.content, "utf-8")

    @property
    def body_object(self):
        """Return deserialized response body"""
        return json.loads(self._response.content)
