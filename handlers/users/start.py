from aiogram import types

from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    try:
        await commands.add_user(int(message.from_user.id))
        await message.answer('Добро пожаловать в sch58 2ch! Все твои сообщения анонимны.\n/enter чтобы зайти в чат\n/help чтобы узнать команды')
    except Exception:
        print("User adding error")
