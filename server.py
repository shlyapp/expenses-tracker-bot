import os
import logging

from aiogram import Bot, Dispatcher, executor, types

import exceptions
import expenses
from categories import Categories
from middlewares import AccessMiddleware


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

try:
    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
    TELEGRAM_ACCESS_ID = os.getenv('TELEGRAM_ACCESS_ID')
    logger.debug("Env variable loaded")
    logger.debug(f"Bot work with user id {TELEGRAM_ACCESS_ID}")
except (ValueError):
    logger.critical(
        "Please, set correct env variables: \n"
        "- TELEGRAM_API_TOKEN\n - TELEGRAM_ACCESS_ID\n")
    raise

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(TELEGRAM_ACCESS_ID))
 

@dp.message_handler(commands=['start', 'help'])
async def send_welocome(message: types.Message):
    await message.answer(f'Привет! Это бот для учета финансов')


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def delete_expense(message: types.Message):
    row_id = int(message.text[4:])
    expenses.delete_expense(row_id)
    await message.answer("Удалил")


@dp.message_handler(commands=['categories'])
async def categories_list(message: types.Message):
    categories = Categories().get_all_categories()
    answer_message = "Категории трат:\n\n" +\
        ("\n* ".join([c.name+' ('+", ".join(c.aliases)+')' for c in categories]))
    await message.answer(answer_message)


@dp.message_handler(commands=['today'])
async def today_statictics(message: types.Message):
    answer_message = expenses.get_today_statistics()
    await message.answer(answer_message)


@dp.message_handler(commands=['month'])
async def month_statictics(message: types.Message):
    answer_message = expenses.get_month_statistics()
    await message.answer(answer_message)


@dp.message_handler(commands=['expenses'])
async def list_expenses(message: types.Message):
    last_expenses = expenses.last()
    if not last_expenses:
        await message.answer("Расходы еще не заведены")
        return

    last_expenses_rows = [
        f"{expense.amount} руб. на {expense.category_name} - нажми "
        f"/del{expense.id} для удаления"
        for expense in last_expenses]
    answer_message = "Последние сохраненные траты:\n\n* " + "\n\n* "\
            .join(last_expenses_rows)
    await message.answer(answer_message)


@dp.message_handler()
async def add_expense(message: types.Message):
    try:
        expense = expenses.add_expense(message.text)
    except exceptions.NotCorrectMessage as e:
        await message.answer(str(e))
        return
    answer_message = (
        f"Добавлены траты {expense.amount} руб. на {expense.category_name}.\n\n"
        f"{expenses.get_today_statistics()}")
    await message.answer(answer_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



