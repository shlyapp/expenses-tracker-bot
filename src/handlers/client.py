from aiogram import types

from keyboards import menu_keyboard
from bot import dp

async def start(message: types.Message):
    await message.answer("Привет, выбери действие!", reply_markup=menu_keyboard)


def register_client_handlers():
    dp.register_message_handler(start, commands=['start'])

