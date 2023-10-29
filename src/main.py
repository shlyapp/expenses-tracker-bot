from aiogram import executor

from bot import dp, bot
from handlers.client import register_client_handlers
from handlers.expenses import register_expense_handler
from handlers.statistics import register_statistics_handler


register_client_handlers()
register_expense_handler()
register_statistics_handler()


executor.start_polling(dp, skip_updates=True)
