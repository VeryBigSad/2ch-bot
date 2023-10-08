from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "начало"),
            types.BotCommand("enter", "зайти в чат"),
            types.BotCommand("exit", "выйти из чата"),
            types.BotCommand("help", "помощь"),
            types.BotCommand("ban", "забанить пользователя"),
            types.BotCommand("unban", "раззабанить пользователя"),
        ]
    )
