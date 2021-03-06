from aiogram import types
from aiogram import Dispatcher
from data.courses_config import courses
from data.config import ADMINS
from states import StudyCourse
from data import emoji
from data.answers import answers_try
import random


async def daily_sending(dp: Dispatcher):
    users_data = await dp.storage.find_all_users()
    admin_logging = []
    for user in users_data:
        user_admin_logging = ''
        course = courses.get(user.get('current_course'))
        user_state = await dp.storage.get_state(chat=user.get('chat'), user=user.get('user'))
        # юзер сдал задание
        if user_state == 'StudyCourse:waiting_for_task':
            new_day = user.get('current_day') + 1
            title = course.get(new_day).get('title')
            description = course.get(new_day).get('description')
            url = course.get(user.get('current_day') + 1).get('url')
            need_answer = course.get(new_day).get('need_answer')

            # если день одинарный, нужно сдать домашку
            if need_answer:
                # проверка на конец курса, если конец - записываем в пройденные и сбрасываем текущий
                if new_day == 14:

                    passed_courses = user.get('passed_courses')
                    if len(passed_courses) == 0:
                        passed_courses = user.get('current_course')
                    else:
                        passed_courses = passed_courses + ',' + user.get('current_course')
                    buttons = ["Супер, спасибо за курс!"]
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    keyboard.add(*buttons)
                    try:
                        await dp.storage.set_state(chat=user.get('chat'), user=user.get('user'),
                                                   state=None)
                        await dp.storage.set_data(chat=user.get('chat'), user=user.get('user'),
                                                  data={'passed_courses': passed_courses,
                                                        'current_course': '',
                                                        'current_day': 0,
                                                        'name': user.get('name')
                                                        })
                        await dp.bot.send_message(user.get('user'), title + '\n' + description + '\n' + url,
                                                  reply_markup=keyboard,
                                                  disable_web_page_preview=True)
                        user_admin_logging = str(user.get('user')) + ' ' + str(user.get('name')) + ' finished course ' + user.get('current_course')
                    except Exception as e:
                        user_admin_logging = str(user.get('user')) + ' get exception ' + str(e)
                # не конец курса
                else:
                    try:
                        await dp.storage.set_state(chat=user.get('chat'), user=user.get('user'),
                                                   state=StudyCourse.waiting_for_homework)
                        await dp.storage.set_data(chat=user.get('chat'), user=user.get('user'),
                                                  data={'passed_courses': user.get('passed_courses'),
                                                        'current_course': user.get('current_course'),
                                                        'current_day': user.get('current_day') + 1,
                                                        'name': user.get('name')
                                                        })
                        buttons = ["Готово, давай дальше", "Нужен еще денёк", "Пропущу это задание"]
                        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                        keyboard.add(*buttons)
                        await dp.bot.send_message(user.get('user'), title + '\n' + description + '\n' + url,
                                                  reply_markup=keyboard)
                        user_admin_logging = str(user.get('user')) + ' ' + str(user.get('name')) + ' is sent ' \
                                             + str(new_day) + ' day in course ' + user.get('current_course')
                    except Exception as e:
                        user_admin_logging = str(user.get('user')) + ' get exception ' + str(e)
            # не нужно сдавать домашку, таких в конце курсов нет
            else:
                try:
                    await dp.storage.set_data(chat=user.get('chat'), user=user.get('user'),
                                              data={'passed_courses': user.get('passed_courses'),
                                                    'current_course': user.get('current_course'),
                                                    'current_day': user.get('current_day') + 1,
                                                    'name': user.get('name')
                                                    })
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    buttons = ["Ок, до завтра"]
                    keyboard.add(*buttons)
                    await dp.bot.send_message(user.get('user'), title + '\n' + description + '\n' + url,
                                              reply_markup=keyboard)
                    user_admin_logging = str(user.get('user')) + ' ' + str(user.get('name')) + ' is sent ' \
                                         + str(new_day) + ' day in course ' + user.get('current_course')
                except Exception as e:
                    user_admin_logging = str(user.get('user')) + ' get exception ' + str(e)
        # юзер не сдал задание
        else:
            if user_state == 'StudyCourse:waiting_for_homework':
                try:
                    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    buttons = ["Готово, давай дальше", "Нужен еще денёк", "Пропущу это задание"]
                    keyboard.add(*buttons)
                    answer = random.choice(answers_try)
                    await dp.bot.send_message(user.get('user'), answer,
                                              reply_markup=keyboard)
                    user_admin_logging = str(user.get('user')) + ' ' + str(user.get('name')) + ' did not pass '\
                                         + str(user.get('current_day')) + ' day in course ' + user.get('current_course')
                except Exception as e:
                    user_admin_logging = str(user.get('user')) + ' get exception ' + str(e)
        if len(user_admin_logging) > 0:
            admin_logging.append(user_admin_logging)
    if len(admin_logging) > 0:
        mess = '\n'.join(admin_logging)
        mess_total = 'Total: ' + str(len(admin_logging)) + ' users'
    else:
        mess = 'Сегодня никому ничего не надо'
        mess_total = 'Total: 0'
    for admin in ADMINS:
        await dp.bot.send_message(admin, mess)
        await dp.bot.send_message(admin, mess_total)

