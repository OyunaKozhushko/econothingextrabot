from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from utils.db_api.courses_config import courses_dict
from loader import dp


@dp.message_handler(Text(equals="Прочитано! Давай дальше :)",
                         ignore_case=True), state='waiting_for_homework')
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    course_name = dp.storage.get_data(chat=chat_id, user=user_id)
    await dp.storage.update_data(chat=chat_id, user=user_id, data={'passed_courses': [],
                                                                   'current_course': course_name,
                                                                   'current_day': 0,
                                                                   'last_homework': 0
                                                                   })
    await dp.storage.set_state(chat=chat_id, user=user_id, state='waiting_for_task')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Ок!"]
    keyboard.add(*buttons)
    await message.answer("Отлично! Завтра пришлю новый материал! Хорошего дня :)", reply_markup=keyboard)

