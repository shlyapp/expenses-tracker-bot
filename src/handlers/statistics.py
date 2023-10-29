from aiogram import types 
from aiogram.dispatcher import FSMContext

from keyboards import statistics_keyboard
from bot import dp
from models.expenses import get_day_statistic, get_interval_statistic
from states import ShowStatistics


async def start_show_statistics(message: types.Message):
    await message.answer("Вы выбрали 'Статистика'", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Пожалуйста, выберите период, за который надо отобразить статистику: ", reply_markup=statistics_keyboard)
    await ShowStatistics.SELECT_INTERVAL.set()


async def select_interval(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(f"Вы выбрали интервал {callback.data}")
    if callback.data == "День":
        await callback.message.answer(get_day_statistic())
    elif callback.data == "Месяц":
        await callback.message.answer(get_interval_statistic())
    await state.finish()
    await callback.answer()


def register_statistics_handler():
    dp.register_message_handler(start_show_statistics, text=['Статистика'])
    dp.register_callback_query_handler(select_interval, state=ShowStatistics.SELECT_INTERVAL)
