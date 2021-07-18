from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from loader import dp


@dp.message_handler(commands="reset")
async def cmd_reset(message: types.Message):
    telegram_id = message.from_user.id
    if telegram_id == '373085647':
        await dp.storage.reset()
        await message.answer('Готово: ', dp.storage.get_db().list_collection_names())
    else:
        await message.answer('Ты кто такой?')

