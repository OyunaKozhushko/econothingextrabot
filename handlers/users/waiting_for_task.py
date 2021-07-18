from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from utils.db_api.courses_config import courses_dict
from loader import dp


@dp.message_handler(Text(equals="Ок!",
                         ignore_case=True), state='waiting_for_homework')
async def course_chosen(message: types.Message):
    return


