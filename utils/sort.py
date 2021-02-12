import json
from itertools import islice


def ordered(obj):
    """
    Returns ordered json object
    """
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def ordered_from_string(string):
    """
    Returns ordered json object of deserialized string
    """
    obj = json.loads(string)
    return ordered(obj)


def chunk_iter(iter_obj, chunk_size):
    """
    Transform iterable into a list of tuples.
    Example,
    >>> chunk_iter([1,2,3,4,5,6,7,8,9], chunk_size=3)
    [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    """
    iter_obj = iter(iter_obj)
    return list(iter(lambda: tuple(islice(iter_obj, chunk_size)), ()))


def sort_key(key):
    """
    Quick wrap of key for sorting
    usage:
    >>> list_ = [{"a": 1, "b": 3}, {"a": 2, "b": 0}]
    >>> sorted(list_, key=sort_key("b"))
    [{"a": 2, "b": 0}, {"a": 1, "b": 3}]
    """
    return lambda i: i[key]
