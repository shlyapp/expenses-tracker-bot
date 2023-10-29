from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import categories_keyboard, comment_keyboard
from bot import dp
from models.expenses import add_expense
from states import AddExpenseState


async def start_add_expense(message: types.Message):
    await message.answer("Вы выбрали 'Добавить расход'.", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Пожалуйста, выберите категорию расходов: ", reply_markup=categories_keyboard)
    await AddExpenseState.CHOOSE_CATEGORY.set()


async def select_category(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(f"Вы выбрали категонрию расходов: '{callback.data}'. Теперь, пожалуйста, введите сумму:")
    async with state.proxy() as data:
        data['category'] = callback.data
    await callback.answer()
    await AddExpenseState.ENTER_AMOUNT.set()


async def enter_expense_amount(message: types.Message, state: FSMContext):
    await message.answer(f"Сумма: {message.text}. Добавить комментарий к расходу?", reply_markup=comment_keyboard)
    async with state.proxy() as data:
        data['amount'] = message.text
    await AddExpenseState.ADD_COMMENT.set()


async def add_comment(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "yes":
        await callback.message.answer("Введите комментарий: ")
        await AddExpenseState.ENTER_COMMENT.set()
    else:
        async with state.proxy() as data:
            data['comment'] = ""
        await finish(callback.message, state)
    await callback.answer()


async def enter_comment(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comment'] = message.text
    await finish(message, state)


async def finish(message: types.Message, state: FSMContext):
    await message.answer("Успешно добавлена новая запись о расходе!")
    async with state.proxy() as data:
        add_expense(data)
        await message.answer(f"{data['category']}, {data['amount']}, {data['comment']}")
    await state.finish()



def register_expense_handler():
    dp.register_message_handler(start_add_expense, text=['Добавить расход'])
    dp.register_callback_query_handler(select_category, state=AddExpenseState.CHOOSE_CATEGORY)
    dp.register_message_handler(enter_expense_amount, state=AddExpenseState.ENTER_AMOUNT)
    dp.register_callback_query_handler(add_comment, state=AddExpenseState.ADD_COMMENT)
    dp.register_message_handler(enter_comment, state=AddExpenseState.ENTER_COMMENT)
