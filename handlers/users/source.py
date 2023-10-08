from aiogram import types

from loader import dp


@dp.message_handler(commands="source")
async def source_command(message: types.Message):
    await message.answer(
        "Исходник бота: https://github.com/verybigsad/2ch-bot\nПоставь звездочку, если знаешь, как пжпжпж"
    )
