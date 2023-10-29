from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

day_statistics = InlineKeyboardButton(text='День', callback_data='День')
month_statistics = InlineKeyboardButton(text='Месяц', callback_data='Месяц')

statistics_keyboard = InlineKeyboardMarkup()
statistics_keyboard.add(day_statistics)
statistics_keyboard.add(month_statistics)
