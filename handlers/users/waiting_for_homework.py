from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from states import StudyCourse
from data import answers, emoji
import random # чтобы выбрать рандомный ответ random.choice(foo)


@dp.message_handler(Text(equals="Прочитано! Давай начинать :)"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    answer = random.choice(answers)
    await dp.storage.set_state(chat=chat_id, user=user_id, state=StudyCourse.waiting_for_task)
    await message.answer(answer, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Готово, давай дальше"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    answer = random.choice(answers)
    await dp.storage.set_state(chat=chat_id, user=user_id, state=StudyCourse.waiting_for_task)
    await message.answer(answer, reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Пропущу это задание"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await dp.storage.set_state(chat=chat_id, user=user_id, state=StudyCourse.waiting_for_task)
    await message.answer("Хорошо! Постарайся пропускать поменьше заданий. Завтра пришлю новый день, удачи сегодня "
                         + emoji.get('hug'),
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Нужен еще денёк"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    buttons = ["Готово, давай дальше", "Нужен еще денёк", "Пропущу это задание"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer("Не вопрос! Не забудь нажать кнопку, когда закончишь. Удачи сегодня " + emoji.get('hug'),
                         reply_markup=keyboard)


@dp.message_handler(Text(equals="Ок, до завтра"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    buttons = ["Готово, давай дальше", "Нужен еще денёк", "Пропущу это задание"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.answer("Не вопрос! Не забудь нажать кнопку, когда закончишь. Удачи сегодня " + emoji.get('hug'),
                         reply_markup=keyboard)