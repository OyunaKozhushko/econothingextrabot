from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.courses_config import courses_dict, courses
from loader import dp
from states import StudyCourse

from data.emoji import emoji


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    first_name = message.from_user.first_name
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    res = await dp.storage.get_data(chat=chat_id, user=telegram_id)
    if not res:
        await dp.storage.set_data(chat=chat_id, user=telegram_id, data={'passed_courses': [],
                                                                        'current_course': '',
                                                                        'current_day': 0
                                                                        })
        await message.answer(f"Привет! Рад знакомству, {first_name}" + emoji.get("hug") +
                             "Я бот проекта Ничего лишнего. У меня есть три полезных курса, которые ты можешь пройти вместе со мной. Каждый курс можно пройти только один раз, длительность курса - 2 недели, но ты можешь делать перерыв, когда захочешь. Каждый день я буду присылать задание, в нем будет и полезный материал, и полезное задание"
                             + emoji.get("relaxed_face"), reply_markup=types.ReplyKeyboardRemove())
        await message.answer("""Первый курс - <strong>Экологичный быт</strong>. Он про то, как сделать ежедневные рутины более экологичными: запустим раздельный сбор отходов, разберемся с холодильником, шкафчиками на кухне и в ванной, познакомимся с натуральной косметикой и избавимся от лишнего в аптечке. А еще удет много идей по организации пространства!""" )
        await message.answer("""Второй - <strong>Осознанный гардероб</strong>. Просто удивительно, как массмаркет изменил наши отношения с одеждой. Теперь у нас очень много вещей - и очень мало среди них тех, которые мы носим. Второй курс поможет разобраться, какие нужными, а какие нет, как экологично избавиться от ненужного, и как осознанно разобрать свой гардероб.""")
        await message.answer("""Третий курс - <strong>Цифровой минимализм</strong>. Он поможет тебе очистить цифровое пространство вокруг себя и тратить меньше времени на такие залипательные вещи, как социальные сети, электронная почта и переписки ни о чем.""")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Экологичный быт", "Осознанный гардероб", "Цифровой минимализм"]
        keyboard.add(*buttons)
        await message.answer("Выбери курс, который хочешь начать " + emoji.get("down_arrow"), reply_markup=keyboard)
    else:
        if res.get("current_course") == '':
            await message.answer(f"Привет! Я бот проекта Ничего лишнего, мы с тобой уже знакомы" +
                                 emoji.get("relieved_face"),
                                 reply_markup=types.ReplyKeyboardRemove())
            passed_courses = res.get("passed_courses")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = []
            if "ecolife" not in passed_courses:
                buttons.append("Экологичный быт")
            if "wardrobe" not in passed_courses:
                buttons.append("Осознанный гардероб")
            if "digital" not in passed_courses:
                buttons.append("Цифровой минимализм")
            buttons.append("Напомни-ка, что у тебя за мини-курсы")
            keyboard.add(*buttons)
            if len(buttons) >= 2:
                text = "Выбери курс, который хочешь начать " + emoji.get("down_arrow")
                await message.answer(text, reply_markup=keyboard)
            else:
                if len(buttons) == 1:
                    text = "Остался всего один курс, жми, если хочешь его пройти " + emoji.get("relieved_face")
                    await message.answer(text, reply_markup=keyboard)
                else:
                    await message.answer("Прости, у меня больше нет курсов, которые я могу тебе предложить "
                                         + emoji.get(""))


@dp.message_handler(Text(equals="Напомни-ка, что у тебя за мини-курсы", ignore_case=True), state=None)
async def course_chosen(message: types.Message, state: FSMContext):
    await message.answer("Конечно! Вот все курсы, которые у меня есть:")
    await message.answer(
        """Первый курс - <strong>Экологичный быт</strong>. Он про то, как сделать ежедневные рутины более экологичными: запустим раздельный сбор отходов, разберемся с холодильником, шкафчиками на кухне и в ванной, познакомимся с натуральной косметикой и избавимся от лишнего в аптечке. А еще удет много идей по организации пространства!""")
    await message.answer(
        """Второй - <strong>Осознанный гардероб</strong>. Просто удивительно, как массмаркет изменил наши отношения с одеждой. Теперь у нас очень много вещей - и очень мало среди них тех, которые мы носим. Второй курс поможет разобраться, какие нужными, а какие нет, как экологично избавиться от ненужного, и как осознанно разобрать свой гардероб.""")
    await message.answer(
        """Третий курс - <strong>Цифровой минимализм</strong>. Он поможет тебе очистить цифровое пространство вокруг себя и тратить меньше времени на такие залипательные вещи, как социальные сети, электронная почта и переписки ни о чем.""")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Экологичный быт", "Осознанный гардероб", "Цифровой минимализм"]
    keyboard.add(*buttons)
    await message.answer("Выбери курс, который хочешь начать " + emoji.get("down_arrow"), reply_markup=keyboard)


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
    day_0 = courses.get(course_name).get(0)
    await message.answer("Отличный выбор! Отправляю вводный материал...\n" +
                         day_0.get('title') + '\n' +
                         day_0.get('description') + '\n' +
                         day_0.get('url')
                         )
    await dp.storage.set_state(chat=chat_id, user=telegram_id, state=StudyCourse.waiting_for_homework)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Прочитано! Давай начинать :)"]
    keyboard.add(*buttons)
    await message.answer("Нажми на кнопку, когда прочтешь вводный материал!", reply_markup=keyboard)


