import json


class BaseModel:
    """
    Base class for API models
    """

    def return_body(self):
        return json.loads(self.return_string())

    def return_string(self):
        return json.dumps(self, default=lambda o: o.__dict__)
