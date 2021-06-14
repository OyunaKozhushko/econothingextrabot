from aiogram import types
from loader import dp


@dp.message_handler(lambda message: message.text == "Экологичный быт")
async def any_text_message(message: types.Message):
    telegram_id = message.from_user.id
    query = {"telegram_id": telegram_id}
    values = {"$set": {"current_course": "ecolife"}}
    mongo_users.update_one(query, values)
#    mongo_courses.find({})
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

