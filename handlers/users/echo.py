from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from data.courses_config import courses_dict, courses_dict_reverse
from loader import dp
from data.emoji import emoji


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Не возьму в толк, о чем речь. Напиши моему создателю <a href='https://t.me/o_lyubimova'>@o_lyubimova</a> или попробуй другую команду "
                         + emoji.get('thinking'),
                         disable_web_page_preview=True)


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer("Не возьму в толк, о чем речь. Напиши моему создателю <a href='https://t.me/o_lyubimova'>@o_lyubimova</a> или попробуй другую команду "
                         + emoji.get('thinking'),
                         disable_web_page_preview=True)



