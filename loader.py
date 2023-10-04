from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)

dp = Dispatcher(bot)