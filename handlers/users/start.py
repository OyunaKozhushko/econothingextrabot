from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from utils.courses_config import courses_dict
from loader import dp
from states import StudyCourse


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer('привет!')
    first_name = message.from_user.first_name
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    res = await dp.storage.get_data(chat=chat_id, user=telegram_id)
    if not res:
        await dp.storage.set_data(chat=chat_id, user=telegram_id, data={'passed_courses': [],
                                                                        'current_course': '',
                                                                        'current_day': 0,
                                                                        'last_homework': 0
                                                                        })
        # await dp.storage.set_state(chat=chat_id, user=telegram_id, state='free')
        await message.answer(f"Привет! Рад знакомству, {first_name}! Я бот проекта Ничего лишнего."
                             f"У меня есть три полезных курса, которые ты можешь пройти вместе со мной.")
        await message.answer("""Первый - Экологичный быт. Он про то, как сделать ежедневные рутины более  
        экологичными: запустим раздельный сбор отходов, разберемся с холодильником, шкафчиками на кухне и в ванной, 
        познакомимся с натуральной косметикой и избавимся от лишнего в аптечке. А еще удет много идей по организации 
        пространства! 
        Второй - Осознанный гардероб. Просто удивительно, как массмаркет изменил наши отношения с 
        одеждой. Теперь у нас очень много вещей - и очень мало среди них тех, которые мы носим. Второй курс поможет 
        разобраться, какие нужными, а какие нет, как экологично избавиться от ненужного, и как осознанно разобрать 
        свой гардероб 
        Третий курс - Цифровой минимализм. Он поможет тебе очистить цифровое пространство вокруг себя 
        и тратить меньше времени на такие залипательные вещи, как социальные сети, электронная почта и переписки  ни 
        о чем.""")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Экологичный быт", "Осознанный гардероб", "Цифровой минимализм"]
        keyboard.add(*buttons)
        await message.answer("Выбери курс, который хочешь начать", reply_markup=keyboard)
    else:
        if res['current_course'] == '':
            await message.answer(f"Привет! Мы с тобой уже знакомы :)")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = ["Экологичный быт", "Осознанный гардероб", "Цифровой минимализм"]
            keyboard.add(*buttons)
            await message.answer("Выбери курс, который хочешь начать", reply_markup=keyboard)


@dp.message_handler(Text(equals=("Экологичный быт", "Осознанный гардероб", "Цифровой минимализм"),
                         ignore_case=True), state=None)
async def course_chosen(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    course_name = courses_dict.get(message.text)
    await dp.storage.update_data(chat=chat_id, user=telegram_id, data={'passed_courses': [],
                                                                       'current_course': course_name,
                                                                       'current_day': 0,
                                                                       'last_homework': 0
                                                                       })
    day_0 = await dp.storage.get_course_day(course_name, 0)
    await message.answer("Отличный выбор! Отправляю вводный материал...\n" +
                         day_0.get('title') + '\n' +
                         day_0.get('description') + '\n' +
                         day_0.get('url')
                         )
    await dp.storage.set_state(chat=chat_id, user=telegram_id, state=StudyCourse.waiting_for_homework)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Прочитано! Давай дальше :)"]
    keyboard.add(*buttons)
    await message.answer("Нажми на кнопку, когда прочтешь вводный материал!", reply_markup=keyboard)


# @dp.message_handler(Text(equals="Прочитано! Давай дальше :)"), state=StudyCourse.waiting_for_homework)
# async def course_chosen(message: types.Message):
#     user_id = message.from_user.id
#     chat_id = message.chat.id
#     await dp.storage.set_state(chat=chat_id, user=user_id, state="waiting_for_task")
#     await message.answer("Отлично! Завтра пришлю новый материал! Хорошего дня :)",
#                          reply_markup=types.ReplyKeyboardRemove())



