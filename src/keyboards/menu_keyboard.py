from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


add_expense = KeyboardButton('Добавить расход')
show_statictics = KeyboardButton('Статистика')

menu_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)
menu_keyboard.add(add_expense)
menu_keyboard.add(show_statictics)
