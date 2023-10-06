from aiogram import types

from loader import dp


@dp.message_handler(commands='help')
async def help_command(message: types.Message):
    await message.answer('Нажмите /start, чтобы зарегистрироваться\n'
                         'Нажмите /enter, чтобы войти в чат\n'
                         'Нажмите /exit, чтобы выйти из чата')
