from aiogram import types
from aiogram.types import ContentType

from data.config import ADMIN_ID
from loader import dp, bot
from utils.db_api import quick_commands as commands


@dp.message_handler(content_types=ContentType.all())
async def chat(message: types.Message):
    status = False
    try:
        status = await commands.get_user_status(message.from_user.id)
    except Exception:
        await message.answer('Press /start to register')

    if status is True:
        try:
            users = await commands.select_all_active_users(message.from_user.id)
            replied_message = None

            if message.reply_to_message:
                replied_message = await bot.copy_message(chat_id=ADMIN_ID, from_chat_id=message.from_user.id,
                                                         message_id=message.reply_to_message.message_id)
            for user in users:
                if message.reply_to_message:
                    await bot.forward_message(chat_id=user.user_id, from_chat_id=ADMIN_ID,
                                              message_id=replied_message.message_id)
                await bot.copy_message(chat_id=user.user_id, from_chat_id=message.from_user.id,
                                       message_id=message.message_id)

            if message.reply_to_message:
                await bot.delete_message(chat_id=ADMIN_ID, message_id=replied_message.message_id)
        except Exception:
            print('Copying error')
    else:
        await message.answer('Press /enter to enter the chat')
