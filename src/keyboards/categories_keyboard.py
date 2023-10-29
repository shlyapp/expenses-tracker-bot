from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from models import Categories, categories


def load_categories_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    categories = Categories().get_all_category()
    for category in categories:
        keyboard.insert(InlineKeyboardButton(text=category, callback_data=category))
    return keyboard


categories_keyboard = load_categories_keyboard()
