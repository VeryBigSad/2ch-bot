from aiogram import types

from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(commands='enter')
async def enter_command(message: types.Message):
    try:
        await commands.update_user_status(message.from_user.id, True)
        await message.answer('Вы зашли в чат')
    except Exception:
        await message.answer('Напиши /start чтобы зарегистрироваться')
        print('Status update error')
