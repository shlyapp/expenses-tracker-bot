import os
from aiogram import Bot, Dispatcher
import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.middlewares import AccessMiddleware

TELEGRAM_API_TOKEN = str(os.getenv("TELEGRAM_API_TOKEN"))
TELEGRAM_ACCOUNT_ID = int(str(os.getenv("TELEGRAM_ACCOUNT_ID")))

bot = Bot(token=TELEGRAM_API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(AccessMiddleware(TELEGRAM_ACCOUNT_ID));
