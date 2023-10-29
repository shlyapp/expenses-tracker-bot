from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


yes_button = InlineKeyboardButton(text="Да", callback_data="yes")
no_button = InlineKeyboardButton(text="Нет", callback_data="no")

comment_keyboard = InlineKeyboardMarkup()
comment_keyboard.insert(yes_button)
comment_keyboard.insert(no_button)


