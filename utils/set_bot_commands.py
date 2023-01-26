from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'start working with bot'),
        types.BotCommand('enter', 'enter to chat'),
        types.BotCommand('exit', 'exit from chat'),
        types.BotCommand('help', 'get help')
    ])
