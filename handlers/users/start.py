from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from data.courses_config import courses_dict, courses, courses_dict_reverse
from loader import dp
from states import StudyCourse

from data.emoji import emoji


# Хэндлер на команду /start
@dp.message_handler(commands="start", state="*")
async def cmd_start(message: types.Message):

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if first_name:
        name = first_name
    else:
        name = ''
    if last_name:
        name = name + ' ' + last_name
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    user_data = await dp.storage.get_data(chat=chat_id, user=telegram_id)
    if not user_data:
        await dp.storage.set_data(chat=chat_id, user=telegram_id, data={'passed_courses': '',
                                                                        'current_course': '',
                                                                        'current_day': 0,
                                                                        'name': name,
                                                                        })
        await message.answer(f"Привет! Рад знакомству, {first_name}" + emoji.get("hug") +
                             "Я бот проекта Ничего лишнего. У меня есть три полезных курса, которые ты можешь пройти вместе со мной. Каждый курс можно пройти только один раз, длительность курса - 2 недели, но ты можешь делать перерыв, когда захочешь. Каждый день я буду присылать задание, в нем будет и полезный материал, и полезное задание "
                             + emoji.get("relaxed_face"), reply_markup=types.ReplyKeyboardRemove())
        await message.answer("""Первый курс - <strong>Экологичный быт</strong>. Он про то, как сделать ежедневные рутины более экологичными: запустим раздельный сбор отходов, разберемся с холодильником, шкафчиками на кухне и в ванной, познакомимся с натуральной косметикой и избавимся от лишнего в аптечке. А еще будет много идей по организации пространства!""")
        await message.answer("""Второй - <strong>Осознанный гардероб</strong>. Просто удивительно, как массмаркет изменил наши отношения с одеждой. Теперь у нас очень много вещей - и очень мало среди них тех, которые мы носим. Второй курс поможет разобраться, какие нужными, а какие нет, как экологично избавиться от ненужного, и как осознанно разобрать свой гардероб.""")
        await message.answer("""Третий курс - <strong>Цифровой минимализм</strong>. Он поможет тебе очистить цифровое пространство вокруг себя и тратить меньше времени на такие залипательные вещи, как социальные сети, электронная почта и переписки ни о чем.""")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Экологичный быт", "Осознанный гардероб", "Цифровой минимализм"]
        keyboard.add(*buttons)
        await message.answer("Выбери курс, который хочешь начать " + emoji.get("down_arrow"), reply_markup=keyboard)
    else:
        if user_data.get("current_course") == '':
            await message.answer(f"Привет! Я бот проекта Ничего лишнего, мы с вами уже знакомы " +
                                 emoji.get("relieved_face"),
                                 reply_markup=types.ReplyKeyboardRemove())
            passed_courses = user_data.get("passed_courses").split(',')
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = []
            for course in list(set(courses_dict.values()) - set(passed_courses)):
                buttons.append(courses_dict_reverse.get(course))
            buttons.append("Напомни-ка, что у тебя за мини-курсы")
            buttons.append("Пока не хочу")
            keyboard.add(*buttons)
            if len(buttons) >= 4:
                text = "Выберите курс, который хотите начать " + emoji.get("down_arrow")
                await message.answer(text, reply_markup=keyboard)
            else:
                if len(buttons) == 3:
                    text = "Остался всего один курс, жмите, если готовы его пройти " + emoji.get("relieved_face")
                    await message.answer(text, reply_markup=keyboard)
                else:
                    await message.answer("Эх, у меня больше нет курсов, которые я могу вам предложить "
                                         + emoji.get("pensive_face"), reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer("Вы сейчас проходите один из моих курсов... Если хотите начать другой, то сначала выполните команду /stop, потом снова /start. Я предложу вам оставшиеся непройденными курсы. Но пройти еще раз текущий курс будет нельзя!")


@dp.message_handler(Text(equals="Напомни-ка, что у тебя за мини-курсы", ignore_case=True), state=None)
async def course_chosen(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    user_data = await dp.storage.get_data(chat=chat_id, user=telegram_id)
    await message.answer("Конечно! Вот все курсы, которые у меня есть:")
    await message.answer(
        """Первый курс - <strong>Экологичный быт</strong>. Он про то, как сделать ежедневные рутины более экологичными: запустим раздельный сбор отходов, разберемся с холодильником, шкафчиками на кухне и в ванной, познакомимся с натуральной косметикой и избавимся от лишнего в аптечке. А еще удет много идей по организации пространства!""")
    await message.answer(
        """Второй - <strong>Осознанный гардероб</strong>. Просто удивительно, как массмаркет изменил наши отношения с одеждой. Теперь у нас очень много вещей - и очень мало среди них тех, которые мы носим. Второй курс поможет разобраться, какие нужными, а какие нет, как экологично избавиться от ненужного, и как осознанно разобрать свой гардероб.""")
    await message.answer(
        """Третий курс - <strong>Цифровой минимализм</strong>. Он поможет тебе очистить цифровое пространство вокруг себя и тратить меньше времени на такие залипательные вещи, как социальные сети, электронная почта и переписки ни о чем.""")

    passed_courses = user_data.get("passed_courses").split(',')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = []
    for course in list(set(courses_dict.values()) - set(passed_courses)):
        buttons.append(courses_dict_reverse.get(course))
    if len(buttons) >= 2:
        buttons.append("Пока не хочу")
        keyboard.add(*buttons)
        text = "Выберите курс, который хотите начать " + emoji.get("down_arrow")
        await message.answer(text, reply_markup=keyboard)
    else:
        if len(buttons) == 1:
            buttons.append("Пока не хочу")
            keyboard.add(*buttons)
            text = "Остался всего один курс, жмите, если готовы его пройти " + emoji.get("relieved_face")
            await message.answer(text, reply_markup=keyboard)
        else:

            await message.answer("Это все! К сожалению, у меня больше нет курсов, которые я могу вам предложить "
                                 + emoji.get("pensive_face"), reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals=("Экологичный быт", "Осознанный гардероб", "Цифровой минимализм"),
                         ignore_case=True), state=None)
async def course_chosen(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    course_name = courses_dict.get(message.text)
    user_data = await dp.storage.get_data(chat=chat_id, user=telegram_id)
    await dp.storage.set_data(chat=chat_id, user=telegram_id, data={
        'passed_courses': user_data.get("passed_courses"),
        'current_course': course_name,
        'current_day': 0,
        'name': user_data.get("name")
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


# прилетает после окончания любого курса
@dp.message_handler(Text(equals="Супер, спасибо за курс!"), state=None)
async def end_course(message: types.Message):
    telegram_id = message.from_user.id
    chat_id = message.chat.id
    user_data = await dp.storage.get_data(user=telegram_id, chat=chat_id)
    passed_courses = user_data.get("passed_courses").split(',')
    buttons = []
    for course in list(set(courses_dict.values()) - set(passed_courses)):
        buttons.append(courses_dict_reverse.get(course))
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    if len(buttons) == 2:
        buttons.append("Напомни-ка, что у тебя за мини-курсы")
        buttons.append("Пока не хочу")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*buttons)
        await message.answer("И вам большое спасибо за прохождение курса " + emoji.get('hug') + '\n' +
                             ' Если есть желание, можете отправить небольшое пожертвование на карту <a href="https://www.tinkoff.ru/cf/4vBDx0qBuSi">Тинькофф по этой ссылке</a>'
                             + ' Сумма абсолютно любая, на ваше усмотрение ' + emoji.get('love_you_gesture'),
                             reply_markup=types.ReplyKeyboardRemove())
        await message.answer("Еще у меня есть два других интересных курса. Если готовы их пройти, то жмите на понравившийся курс. Если пока неинтересно - жмите на кнопку 'Пока не хочу' "
                             + emoji.get('down_arrow'), reply_markup=keyboard)
    else:
        if len(buttons) == 1:
            buttons.append("Напомни-ка, что у тебя за мини-курсы")
            buttons.append("Пока не хочу")
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*buttons)
            await message.answer("И вам большое спасибо за прохождение курса " + emoji.get('hug') + '\n' +
                                """ Если есть желание, можете отправить небольшое пожертвование на карту <a href="https://www.tinkoff.ru/cf/4vBDx0qBuSi">Тинькофф по этой ссылке</a>. Сумма абсолютно любая, на ваше усмотрение """ + emoji.get('love_you_gesture'),
                                 reply_markup=types.ReplyKeyboardRemove())
            await message.answer("У меня есть еще один интересный курс. Если готовы пройти, то жмите на кнопку с курсом. Если пока неинтересно - жмите на кнопку 'Пока не хочу' "
                                 + emoji.get('down_arrow'), reply_markup=keyboard)
        else:
            buttons = ["Счастливо!"]
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*buttons)
            await message.answer("И вам большое спасибо за прохождение курса " + emoji.get('hug') + '\n' +
                                 """ Если есть желание, можете отправить небольшое пожертвование на карту <a href="https://www.tinkoff.ru/cf/4vBDx0qBuSi">Тинькофф по этой ссылке</a>. Сумма абсолютно любая, на ваше усмотрение """ + emoji.get('love_you_gesture'),
                                 reply_markup=types.ReplyKeyboardRemove())
            await message.answer("У меня больше нет непройденных вами курсов! Удачи вам во всех начинаниях!",
                                 reply_markup=keyboard)


# прилетает после завершения вообще всего
@dp.message_handler(Text(equals="Счастливо!"), state=None)
async def final_end(message: types.Message):
    await message.answer("Пока-пока! " + emoji.get('relieved_face'), reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(Text(equals="Пока не хочу"), state=None)
async def not_want(message: types.Message):
    await message.answer("Не вопрос! Пишите команду /start, когда будете готовы, начнем"
                         + emoji.get('winking_face'), reply_markup=types.ReplyKeyboardRemove())
