from aiogram import types
from loader import dp


# Хэндлер на команду /stop
@dp.message_handler(commands="stop")
async def cmd_stop(message: types.Message):
    # todo stop messaging
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_data = await dp.storage.get_data(chat=chat_id, user=user_id)
    await dp.storage.set_data(chat=chat_id, user=user_id, data={'passed_courses': user_data.get(
        'passed_courses').append(user_data.get('current_course')),
                                                                'current_course': '',
                                                                'current_day': 0
                                                                })
    await dp.storage.set_state(chat=chat_id, user=user_id, state=None)
    await message.answer("Хорошо! Больше тебя не беспокою) Если захочешь вернуться - напиши /start, я снова буду "
                         "активен", reply_markup=types.ReplyKeyboardRemove())
