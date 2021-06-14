from aiogram import types
from loader import dp


# Хэндлер на команду /stop
@dp.message_handler(commands="stop")
async def cmd_stop(message: types.Message):
    # todo stop messaging
    await message.answer("Я так больше не играю :(")
