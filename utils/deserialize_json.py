"""
JSON deserialization.
"""
import json


def deserialize_json_file(json_file):
    with open(json_file, mode='r') as obj_:
        data = json.load(obj_)
    return data
