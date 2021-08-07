from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(Text(equals="Ок!",
                         ignore_case=True), state='waiting_for_homework')
async def course_chosen(message: types.Message):

    return


