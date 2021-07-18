from aiogram import Bot, Dispatcher, types
from states import MongoStorage

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MongoStorage(host='localhost', port=27017, db_name='econothingextra_mongodb')
dp = Dispatcher(bot, storage=storage)
