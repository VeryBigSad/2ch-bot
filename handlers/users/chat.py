from aiogram import types
from aiogram.types import ContentType
from data.config import ALLOW_GIFS

from loader import dp, bot
from utils.db_api import quick_commands as commands


@dp.message_handler(content_types=ContentType.all())
async def chat(message: types.Message):
    status = False
    try:
        status = await commands.get_user_status(message.from_user.id)
    except Exception:
        await message.answer('Нажми /start чтобы зарегистрироваться')

    if message.content_type == 'animation' and not ALLOW_GIFS:
        await message.answer('Пока без гифок :(')
        return

    is_banned = await commands.is_banned(message.from_user.id)
    if is_banned:
        await message.answer('Вы забанены :(\nНаверное, вы вели себя очень плохо...')
        return

    if status is True:
        try:
            await commands.add_message(message.from_user.id, message.message_id, message.message_id)
            users = await commands.select_all_active_users(message.from_user.id)
            original_id = None

            if message.reply_to_message:
                try:
                    original_id = await commands.get_original_message(
                        message.from_user.id,
                        message.reply_to_message.message_id
                    )
                except Exception:
                    await message.answer('Это сообщение слишком старое!')

            for user in users:
                try:
                    replied_id = None

                    if message.reply_to_message:
                        replied_id = await commands.get_replied_message(user.user_id, original_id)

                    copied_message = await bot.copy_message(
                        chat_id=user.user_id,
                        from_chat_id=message.from_user.id,
                        message_id=message.message_id,
                        reply_to_message_id=replied_id
                    )
                    await commands.add_message(user.user_id, message.message_id, copied_message.message_id)
                except Exception:
                    print('Copying error')

            await commands.refresh_messages()
        except Exception:
            print('Chat handler error')
    else:
        await message.answer('Напиши /enter чтобы зайти в чат')
