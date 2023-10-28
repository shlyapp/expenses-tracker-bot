from sqlite3 import Cursor
from typing import NamedTuple, Optional
import datetime

import database.db
from utils import get_now_formatted, get_now_datetime


class Message(NamedTuple):
    amount: int
    comment_text: str


class Expense(NamedTuple):
    id: Optional[int]
    amount: int
    category_name: str
    comment_text: str


def add_expense(raw_message: str, category_name: str) -> None:
    message = _parse_message(raw_message)
    database.db.insert("expense", {
        "amount": message.amount,
        "created": get_now_formatted(),
        "category_name": category_name,
        "comment_text": message.comment_text
        })


def remove_expense(id: int) -> None:
    database.db.delete("expense", id)


def get_day_statistic(date: datetime.datetime) -> str:
    cursor = database.db.get_cursor()
    cursor.execute("SELECT sum(amount) "
                   "FROM expense WHERE date(created) = date('now', 'localtime')")
    result = cursor.fetchone()
    if not result[0]:
        return "Нет расходов за сегодня"
    return f"Сумма расходов за сегодня: {result[0]}"


def get_interval_statistic(date_start: datetime.datetime, date_end: datetime.datetime) -> str:
    now = get_now_datetime()
    first_day_of_month = f'{now.year:04d}-{now.month:02d}-01'
    cursor = database.db.get_cursor()
    cursor.execute(f"SELECT sum(amount) "
                   f"FROM expense WHERE date(created) >= '{first_day_of_month}'")
    result = cursor.fetchone()
    if not result[0]:
        return "В этом месяце еще нет расходов"
    return result[0]


def _parse_message(raw_message: str) -> Message:
    parts = raw_message.split()
    message = Message(int(parts[0]), parts[1])
    return message
