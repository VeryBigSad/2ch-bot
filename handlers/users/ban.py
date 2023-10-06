from aiogram import types

from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(commands='ban')
async def ban_command(message: types.Message):
    is_admin = await commands.is_admin(message.from_user.id)
    if is_admin:
        reply_id = message.reply_to_message.from_user.id
        await commands.set_is_banned(reply_id, False)
        await message.answer('Пользователь забанен')
    else:
        await message.answer('Ты без прав :(')