import os

from aiogram import Bot, Dispatcher, executor, types

from middlewares import AccessMiddleware


TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TELEGRAM_ACCESS_ID = os.getenv('TELEGRAM_ACCESS_ID')

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(AccessMiddleware(TELEGRAM_ACCESS_ID))


@dp.message_handler(commands=['start', 'help'])
async def send_welocome(message: types.Message):
    await message.answer(f'Hello, {message.from_user.id}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



