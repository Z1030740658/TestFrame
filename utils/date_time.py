"""
Converts object to datetime format.
"""
import functools
from datetime import datetime, timedelta
from time import time
from tzlocal import get_localzone

import pytz

from utils.logger import log

import humanreadable


def gen_log_dates(past_days=7, tz=None):
    """
    Generate log dates.
    Example, if today is 2020-09-01 and past_days=3,
        it returns today's date and 3 days in the past, so it's going to be a list of 4 items:
        ['2020-09-01', '2020-08-31', '2020-08-30', '2020-08-29']
    """
    if not tz:
        tz = "UTC"
    ptz = pytz.timezone(tz)

    log_dates = []
    today = datetime.now(tz=ptz)

    for pd in range(0, past_days + 1):
        d = timedelta(days=pd)
        log_date = today - d
        log_dates.append(log_date.strftime("%Y-%m-%d"))
    return log_dates


def now_iso_time(zulu_frmt=True):
    """
    Returns now time in ISO 8601 format in UTC
    :param zulu_frmt: if True return zulu time format, e.g. '2020-11-26T13:51:29Z',
        otherwise return string with UTC offset, e.g. '2020-11-26T13:51:29+00:00'
    """
    time_now = datetime.utcnow().replace(tzinfo=pytz.UTC).replace(microsecond=0).isoformat()
    if zulu_frmt:
        time_now = time_now.replace("+00:00", "Z")
    return time_now


def timestamp_ms():
    """
    Get current timestamp in milliseconds.
    """
    return int(time() * 1000)


def milliseconds(human_time_format):
    """
    Kind of magic method to convert time in human readable format into milliseconds.
    It leverages 'humanreadable' package, for more details/example check project's doc on PyPi.
    :param human_time_format: str representing some time delta, e.g '1d 3h 5m', '2days 3hours 25minutes' etc.
    """
    # Split all values by whitespace as 'humanreadable' recognizes one time unit in one string value
    split_units = human_time_format.split(" ")
    millis_units = [humanreadable.Time(unit_value).milliseconds for unit_value in split_units]
    return int(functools.reduce(lambda x, y: x + y, millis_units))


def string_to_date_time(string_time, format_):
    """
    Convert date time presented in string to date time object based on provided format, 
    for example it could be: "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ".
    """
    log.info(f"DATE TIME IS: {string_time}")
    return datetime.strptime(string_time, format_).replace(tzinfo=pytz.UTC).replace(microsecond=0)


def is_today(date_time):
    """
    Verify if provided date time object date is the same as today date.
    """
    today = datetime.utcnow().date()
    log.debug(f"DATE TIME IS: {date_time}, TODAY IS: {today}")
    return date_time.date() == today


def timestamp_to_iso(timestamp, tz=pytz.UTC):
    """
    Convert timestamp to ISO time (UTC only)
    """
    return datetime.fromtimestamp(timestamp, tz=tz).replace(microsecond=0).isoformat()


def utc_to_local_timezone(date_time):
    log.info(f"AS UTC TIME: {date_time.astimezone(tz=pytz.timezone('UTC'))}")
    log.info(f"TIMEZONE NAME : {datetime.now().astimezone().tzname()}")
    log.info(f"UTC TO TIMEZONE: {date_time.astimezone(get_localzone())}")
    return datetime.fromtimestamp(datetime.timestamp(date_time), get_localzone())
