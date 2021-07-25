import logging
from aiogram import Dispatcher


async def daily_sending(dp: Dispatcher):
    dp.storage.get_data()
    await dp.bot.send_message(373085647, 'new day')


#{'_id': ObjectId('60a011ff3710c8837b90f731'), 'telegram_id': 373085647, 'chat_id': 373085647,
# 'current_course': 'ecolife', 'current_day': 0, 'passed_courses': []}

