from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    text = ("Вот список моих команд: ",
            "/start - выбрать и начать курс",
            "/help - посмотреть команды",
            "/stop - завершить курс",
            "/donate - помочь проекту")
    
    await message.answer("\n".join(text))
    await message.answer("Всего у меня три курса: Экологичный быт, Осознанный гардероб, Цифровой минимализм. Любой из курсов можно пройти любой из них один раз. Каждый курс длится две недели, в нем до 14 разных материалов и к каждому материалу есть практическое задание. Только практика ведет к изменениям, поэтому без заданий никуда. После выполнения задания жмите на кнопку - и на следующий день я пришлю новый материал :) Если есть вопросы, можешь написать моему создателю: <a href='https://t.me/o_lyubimova'>@o_lyubimova</a>",
                         disable_web_page_preview=True)

