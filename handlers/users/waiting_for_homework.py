from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from states import StudyCourse
import random # чтобы выбрать рандомный ответ random.choice(foo)
# TODO добавить рандомыне ответы


async def check_for_last_day(chat_id, user_id):
    user_data = await dp.storage.get_data(chat=chat_id, user=user_id)
    if user_data.get('current_day') == 14:
        await dp.storage.set_data(chat=chat_id, user=user_id, data={'passed_courses': user_data.get(
            'passed_courses').append(user_data.get('current_course')),
                                                                    'current_course': '',
                                                                    'current_day': 0
                                                                    })
        await dp.storage.set_state(chat=chat_id, user=user_id, state=None)
        await dp.bot.send_message(user_id, 'Поздравляю с завершением курса! Ты молодец!',
                                  reply_markup=types.ReplyKeyboardRemove())
        if len(user_data.get('passed_courses')) < 2:
            await dp.bot.send_message(user_id, 'Если тебе понравилось, посмотри другие мои курсы')
        else:
            await dp.bot.send_message(user_id, 'Спасибо тебе большое! К сожалению, у меня больше нет курсов, '
                                               'чтобы предложить тебе. Подпишись на мой инстаграм, если еще нет, '
                                               'я буду публиковать там разную полезную информацию - в том же стиле и '
                                               'смысловом наполнении. До встречи :)')


@dp.message_handler(Text(equals="Прочитано! Давай начинать :)"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await dp.storage.set_state(chat=chat_id, user=user_id, state=StudyCourse.waiting_for_task)
    await message.answer("Отлично! Завтра пришлю новый материал! Хорошего дня :)",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Готово, давай дальше :)"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await dp.storage.set_state(chat=chat_id, user=user_id, state=StudyCourse.waiting_for_task)
    await message.answer("Ты молодец! Завтра пришлю новый материал! Хорошего дня :)",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Пропущу этот день"), state=StudyCourse.waiting_for_homework)
async def course_chosen(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    await dp.storage.set_state(chat=chat_id, user=user_id, state=StudyCourse.waiting_for_task)
    await message.answer("Хорошо! Постарайся пропускать поменьше заданий. Завтра пришлю новый день, удачи сегодня :)",
                         reply_markup=types.ReplyKeyboardRemove())

