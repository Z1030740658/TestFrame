from utils.logger import log
"""
Compares two python objects or lists, or objects within lists
"""


def equal_dictionaries(a, b, ignore_keys=None):
    """
    Two objects comparison. To exclude property from comparison, provide property name within ignore_keys.
    """
    log.info(f"OBJ A: {a}")
    log.info(f"OBJ B: {b}")
    set_a = set(a)
    set_b = set(b)
    if ignore_keys:
        excl_a = set(ignore_keys).difference(set_a)
        excl_b = set(ignore_keys).difference(set_b)
        if bool(excl_a) or bool(excl_b):
            log.debug(f"NO SUCH PROPERTIES IN OBJECT FOUND: {excl_a}, {excl_b}")
        ka = set_a.difference(ignore_keys)
        kb = set_b.difference(ignore_keys)
        if equal_lists(ka, kb) is False:
            log.info(f"DIFFERENCE IN: {ka}, {kb}")
            return False
        elif all(a[k] == b[k] for k in ka):
            return True
        else:
            for k in ka:
                if a[k] != b[k]:
                    log.info(f"DIFFERENCE IN: {k}; VALUES ARE: {a[k]}, {b[k]}")
            return False
    else:
        return all(k in a and a[k] == v for k, v in b.items())


def equal_lists(list_a, list_b):
    if any(x in list_a for x in list_b) is not True:
        log.info(f"DIFFERENCE IN LISTS OF OBJECTS: {[i for i in list_a if i not in list_b]}")
        return False
    else:
        return True


def find_by_object_property(list_, **kwargs):
    """
    Example: having listOfDicts=[{'foo':1, 'bar':2, 'x':55, 'y': 77 },{'foo':1, 'bar':2, 'x':66, 'z': 88 }].
    By passing list and property of object in list you are looking for: find_by_object_property(listOfDicts, x=55).
    Shall result in {'foo':1, 'bar':2, 'x':55, 'y': 77 }.
    """
    log.info(f"LOOKING IN LIST: {list_}")
    return next(item for item in list_ if list_.match(**kwargs))


def find_by_property_in_list(list_, property_, value):
    """
    Example: having listOfDicts=[{"id":1,"name":"ronaldo"},{"id":2,"name":"messi"}]
    By passing list and property of object in list you are looking for:
    find_by_property_in_list(listOfDicts, 'name', 'ronaldo').
    Shall result in {"id":1,"name":"ronaldo"}.
    """
    log.info(f"LOOKING IN LIST: {list_} OF PROPERTY: {property_} WITH VALUE: {value}")
    return next((x for x in list_ if x[property_] == value), None)


def return_all_props_with_none_value(object_):
    return [key for key, value in object_.items() if value is None]


def return_values_from_list_of_objects(list_, property_):
    """
    Example: having list_=[{"id":1,"name":"ronaldo"},{"id":2,"name":"messi"}]
    By passing list and property name you are looking for:
    return_values_from_list_of_objects(list_, 'id').
    Shall result in [1,2].
    """
    return [d['property_'] for d in list_ if 'property_' in d]
