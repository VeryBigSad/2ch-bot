from aiogram import types
from aiogram.types import ContentType

from data.config import GROUP_ID
from loader import dp, bot
from utils.db_api import quick_commands as commands


@dp.message_handler(content_types=ContentType.POLL)
async def poll(message: types.Message):
    try:
        copied_poll = await message.copy_to(GROUP_ID)
        users = await commands.select_all_active_users(message.from_user.id)

        for user in users:
            await bot.forward_message(
                chat_id=user.user_id,
                from_chat_id=GROUP_ID,
                message_id=copied_poll.message_id,
            )
    except Exception:
        print("Poll copying error")
