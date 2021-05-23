from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from data.config import *


def create_new_user(telegram_id: int, chat_id: int):
    try:
        mongo_users.insert_one({'telegram_id': telegram_id,
                                'chat_id': chat_id,
                                'current_course': '',
                                'current_day': 0,
                                'passed_courses': []
                                })
    except:
        return False
    return True


@dp.message_handler(lambda message: message.text == "Экологичный быт")
async def any_text_message(message: types.Message):
    telegram_id = message.from_user.id
    query = {"telegram_id": telegram_id}
    values = {"$set": {"current_course": "ecolife"}}
    mongo_users.update_one(query, values)
    mongo_courses.find({})
    await message.answer("Ок! Отправляю предварительный материал. Завтра будет первый день!",
                         reply_markup=types.ReplyKeyboardRemove())
    await message.answer()


@dp.message_handler(lambda message: message.text == "Осознанный гардероб")
async def any_text_message(message: types.Message):
    telegram_id = message.from_user.id
    query = {"telegram_id": telegram_id}
    values = {"$set": {"current_course": "wardrobe"}}
    mongo_users.update_one(query, values)
    await message.answer("Ок! Отправляю предварительный материал. Завтра будет первый день!",
                         reply_markup=types.ReplyKeyboardRemove())


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    first_name = message.from_user.first_name
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    query = {"telegram_id": telegram_id}
    if mongo_users.count_documents(query) == 0 & ~message.from_user.is_bot:
        if create_new_user(telegram_id, chat_id):
            await message.answer(f"Привет! Рад знакомству, {first_name}! Я бот проекта Ничего лишнего. Давай играть!")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Экологичный быт", "Осознанный гардероб"]
            keyboard.add(*buttons)
            await message.answer("Выбери курс, который хочешь начать", reply_markup=keyboard)
    else:
        user_stat = mongo_users.find(query)
        await message.answer(f"Привет! Я тебя знаю: ты сейчас проходишь курс!")
    # await message.answer(f"Привет, {first_name}! Я бот проекта Ничего лишнего. Давай играть!")


# Хэндлер на команду /stop
@dp.message_handler(commands="stop")
async def cmd_stop(message: types.Message):
    # todo stop messaging
    await message.answer("Я так больше не играю :(")
