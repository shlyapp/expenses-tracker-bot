import datetime
import pytz


def get_now_formatted() -> str:
    return get_now_datetime().strftime("%Y-%m-%d %H:%M:%S")


def get_now_datetime() -> datetime.datetime:
    tz = pytz.timezone("Europe/Samara")
    now = datetime.datetime.now(tz)
    return now
