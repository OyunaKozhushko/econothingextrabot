from aiogram import types
from loader import dp
from data.emoji import emoji


# Хэндлер на команду /donate
@dp.message_handler(commands="donate", state="*")
async def cmd_donate(message: types.Message):
    await message.answer("Спасибо за поддержку! Для меня очень важно видеть, что проект приносит пользу " + emoji.get("hug") +
                         ' Вы можете отправить пожертвование карту <a href="https://www.tinkoff.ru/cf/4vBDx0qBuSi">Тинькофф по этой ссылке</a>'
                         + ' Сумма абсолютно любая, на ваше усмотрение ' + emoji.get('love_you_gesture'),
                         reply_markup=types.ReplyKeyboardRemove())


