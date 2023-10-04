from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

async def on_startup(dp):
    print("Bot started")