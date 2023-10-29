from aiogram import types

from loader import dp
from data.config import SOURCE_URL


@dp.message_handler(commands="source")
async def source_command(message: types.Message):
    await message.answer(
        f"Исходник бота: {SOURCE_URL}\nПоставь звездочку пжпж (если знаешь как) <3"
    )
