from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp
from states import StudyCourse


@dp.message_handler(Text(equals="Прочитано! Давай дальше :)"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await dp.storage.set_state(chat=chat_id, user=user_id, state="waiting_for_task")
    await message.answer("Отлично! Завтра пришлю новый материал! Хорошего дня :)",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Готово! Давай дальше :)"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await dp.storage.set_state(chat=chat_id, user=user_id, state="waiting_for_task")
    await message.answer("Ты молодец! Завтра пришлю новый материал! Хорошего дня :)",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Пропущу"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await dp.storage.set_state(chat=chat_id, user=user_id, state="waiting_for_task")
    await message.answer("Хорошо! Постарайся пропускать поменьше заданий. Завтра пришлю новый день, удачи сегодня :)",
                         reply_markup=types.ReplyKeyboardRemove())

