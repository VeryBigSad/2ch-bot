from aiogram import types

from loader import dp
from utils.db_api import quick_commands as commands


@dp.message_handler(commands="ban")
async def ban_command(message: types.Message):
    is_admin = await commands.is_admin(message.from_user.id)
    if is_admin:
        replied_user_id = await commands.get_replied_message_creator(message.from_user.id, message.reply_to_message.message_id)
        await commands.set_is_banned(replied_user_id, True)
        await message.answer("Пользователь забанен")
    else:
        await message.answer("Ты без прав :(")

    
@dp.message_handler(commands="unban")
async def ban_command(message: types.Message):
    is_admin = await commands.is_admin(message.from_user.id)
    if is_admin:
        replied_user_id = await commands.get_replied_message_creator(message.from_user.id, message.reply_to_message.message_id)
        await commands.set_is_banned(replied_user_id, False)
        await message.answer("Пользователь разбанен")
    else:
        await message.answer("Ты без прав :(")
