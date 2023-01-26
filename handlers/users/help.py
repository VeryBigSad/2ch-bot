from aiogram import types

from loader import dp


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.answer('Press /start to register\n'
                         'Press /enter to enter to chat\n'
                         'Press /exit to exit from chat')
