"""
Converts object to datetime format.
"""
from datetime import datetime


def load_with_datetime(pairs, format='%Y-%m-%d'):
    """Load with dates"""
    d = {}
    for k, v in pairs:
        if isinstance(v, str):
            try:
                d[k] = datetime.strptime(v, format).date()
            except ValueError:
                d[k] = v
        else:
            d[k] = v             
    return d
