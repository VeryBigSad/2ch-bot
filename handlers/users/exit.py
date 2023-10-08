from aiogram import types

from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(commands="exit")
async def exit_command(message: types.Message):
    try:
        await commands.update_user_status(message.from_user.id, False)
        await message.answer("Вы вышли из чата")
    except Exception:
        await message.answer("Напиши /start чтобы зарегистрироваться")
        print("Status update error")
