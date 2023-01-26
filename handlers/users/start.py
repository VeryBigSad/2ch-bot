from aiogram import types

from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    try:
        await commands.add_user(int(message.from_user.id))
        await message.answer('Welcome to Inno2ch!\nPress /enter to enter to chat\nPress /help for help')
    except Exception:
        print("User adding error")
