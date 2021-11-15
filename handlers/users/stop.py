from aiogram import types
from loader import dp
from data.emoji import emoji


# Хэндлер на команду /stop
@dp.message_handler(commands="stop", state="*")
async def cmd_stop(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_data = await dp.storage.get_data(chat=chat_id, user=user_id)
    passed_courses = user_data.get('passed_courses')
    if len(passed_courses) == 0:
        passed_courses = user_data.get('current_course')
    else:
        passed_courses = passed_courses + ',' + user_data.get('current_course')
    await dp.storage.set_data(chat=chat_id, user=user_id, data={'passed_courses': passed_courses,
                                                                'current_course': '',
                                                                'current_day': 0
                                                                })
    await dp.storage.set_state(chat=chat_id, user=user_id, state=None)
    await message.answer("Хорошо! Больше не беспокою " + emoji.get("raising_hands") +
                         " Этот курс пометил завершенным, если захотите пройти другой курс - напишите /start, я предложу доступные курсы "
                         + emoji.get("hug"),
                         reply_markup=types.ReplyKeyboardRemove())


