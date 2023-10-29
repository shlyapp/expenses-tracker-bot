from aiogram.dispatcher.filters.state import State, StatesGroup


class ShowStatistics(StatesGroup):
    SELECT_INTERVAL = State()
    SHOW_STATISTICS = State()

