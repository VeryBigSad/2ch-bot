from aiogram import Bot, types, Dispatcher

from data import config
from utils.db_api.db_gino import db

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

__all__ = ['bot', 'dp', 'db']
