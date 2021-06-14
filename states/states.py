from aiogram.dispatcher.filters.state import State, StatesGroup


class StudyCourse(StatesGroup):
    free = State()  # ничего не изучает
    waiting_for_task = State()  # ждет следующее задание
    waiting_for_homework = State() # делает домашку


