import logging
from aiogram import Bot, Dispatcher, executor, types
from pymongo import MongoClient
import apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio


API_TOKEN = "1708953167:AAHL5jCYsCovCxYQxgt_ZlRC1eSJxoFe-34"

# Объект бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

client = MongoClient("mongodb://localhost:27017/")
db = client['dbbot']
mongo_users = db['users']
mongo_courses = db['courses']

scheduler = AsyncIOScheduler()


async def daily_sending(dp):
    #for x in mongo_users.find():
    #    if (x['current_course'] != '') & (x['current_day'] != 14):
    await dp.bot.send_message(373085647, 'new B day')


async def schedule_jobs():
    scheduler.add_job(daily_sending, 'interval', seconds=5, args=(dp,))


async def on_startup(dp):
    await schedule_jobs()


#{'_id': ObjectId('60a011ff3710c8837b90f731'), 'telegram_id': 373085647, 'chat_id': 373085647,
# 'current_course': 'ecolife', 'current_day': 0, 'passed_courses': []}


if __name__ == "__main__":
    # Запуск бота
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
    # executor.start_polling(dp, skip_updates=True, on_startup=on_start)
    # asyncio.run(daily_sending())
