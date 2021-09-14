from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from data import emoji


@dp.message_handler(Text(equals="Ок, до завтра",
                         ignore_case=True), state='waiting_for_homework')
async def skip_extra_day(message: types.Message):
    await message.answer('Привет! Вчерашнее задание - на два дня, так что сегодня - отдых. Хорошего тебе дня'
                         + emoji.get('hug'), reply_markup=types.ReplyKeyboardRemove())
    return


