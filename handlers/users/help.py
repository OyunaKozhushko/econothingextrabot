from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = ("Вот список моих команд: ",
            "/start - начать проходить курс",
            "/stop - завершить курс")
    
    await message.answer("\n".join(text))
    await message.answer("Всего у меня три курса: Экологичный быт, Осознанный гардероб, Цифровой минимализм. Ты "
                         "можешь пройти любой из них один раз. Каждый курс длится две недели, в нем от 10 до 14 "
                         "материалов и к каждому материалу есть практическое задание. Только практика везет к "
                         "изменениям, поэтому без заданий никуда. Выполняешь задание - на следующий день я пришлю "
                         "новый материал :) Если есть вопросы, можешь написать моему создателю: @o_lyubimova")
    # TODO добавить ссылку на телегу

