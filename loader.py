from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import math
import time
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.MARKDOWN)

dp = Dispatcher(bot)
