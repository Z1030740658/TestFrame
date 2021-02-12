import math


def col_round(x):
    """
    As Python 3 rounds 0.5 fraction to closest even,
    floor and cell round methods used here to round 0.5
    up to next digit and 0.4 down back to previos.
    """
    frac = x - math.floor(x)
    if frac < 0.5:
        return math.floor(x)
    return math.ceil(x)
