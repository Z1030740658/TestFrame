"""
JSON deserialization.
"""
import json


def deserialize_json(json_):
    with open(json_, mode='r') as obj_:
        data = json.load(obj_)
    return data
