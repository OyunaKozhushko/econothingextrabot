from aiogram import Bot, Dispatcher, types
from states import MongoStorage
from data import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.daily import daily_sending
from datetime import datetime

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MongoStorage(host='localhost', port=27017, db_name='econothingextra_mongodb')
dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
scheduler.add_job(daily_sending, "cron", second=43, args=(dp,))

