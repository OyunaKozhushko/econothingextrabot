from aiogram import Bot, Dispatcher, types
from states import MongoStorage
from data import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.daily import daily_sending
from datetime import datetime

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MongoStorage(db_name=config.db_name, host=config.db_host, username=config.db_user, password=config.db_password)

dp = Dispatcher(bot, storage=storage)
scheduler = AsyncIOScheduler()
scheduler.add_job(daily_sending, "cron", hour=4, minute=5, args=(dp,), timezone='UTC')
# scheduler.add_job(daily_sending, "interval", seconds=10, args=(dp,))
