from aiogram import types
from aiogram.types import ContentType

from data.config import GROUP_ID
from loader import dp


@dp.message_handler(content_types=ContentType.POLL)
async def poll(message: types.Message):
    try:
        await message.copy_to(GROUP_ID)
    except Exception:
        print('Poll copying error')
