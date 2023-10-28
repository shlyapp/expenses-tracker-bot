from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

day_statistics = KeyboardButton('День')
week_statistics = KeyboardButton('Неделя')
month_statistics = KeyboardButton('Месяц')

statistics_keyboard = ReplyKeyboardMarkup()
statistics_keyboard.add(day_statistics)
statistics_keyboard.add(week_statistics)
statistics_keyboard.add(month_statistics)
