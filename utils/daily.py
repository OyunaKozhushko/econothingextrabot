import logging
from aiogram import types
from aiogram import Dispatcher
from utils.courses_config import courses
from states import StudyCourse


async def daily_sending(dp: Dispatcher):
    users_data = await dp.storage.find_all_users()
    for user in users_data:
        course = courses.get(user.get('current_course'))
        # TODO проверить, что дата не последняя и ваще есть нужный день
        # TODO проверить, что домашка сделана (нужный state у юзера)
        title = course.get(user.get('current_day')+1).get('title')
        description = course.get(user.get('current_day')+1).get('description')
        url = course.get(user.get('current_day')+1).get('url')
        await dp.storage.set_state(chat=user.get('chat'), user=user.get('user'), state=StudyCourse.waiting_for_homework)
        await dp.storage.set_data(chat=user.get('chat'), user=user.get('user'), data={'passed_courses': [],
                                                                        'current_course': user.get('current_course'),
                                                                        'current_day': user.get('current_day')+1
                                                                        })
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Готово, давай дальше :)", "Пропущу этот день"]
        keyboard.add(*buttons)
        await dp.bot.send_message(user.get('user'), title + '\n' + description + '\n' + url,
                                  reply_markup=keyboard)
        # await dp.bot.send_message(373085647, 'new day')


