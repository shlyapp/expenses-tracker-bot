from aiogram.dispatcher.filters.state import State, StatesGroup


class AddExpenseState(StatesGroup):
    CHOOSE_CATEGORY = State()
    ENTER_AMOUNT = State()
    ADD_COMMENT = State()

