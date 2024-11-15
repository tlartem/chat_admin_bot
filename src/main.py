import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command

import config
from handlers import (
    add_chat,
    cmd_start,
    handle_message,
    support,
    user_chats,
)
from utils.commands import send_bot_started_message, send_bot_stopped_message


async def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    bot = Bot(token=config.BOT_TOKEN)

    dp = Dispatcher()

    if not config.DEBUG:
        dp.startup.register(send_bot_started_message)
        dp.shutdown.register(send_bot_stopped_message)

    dp.message.register(cmd_start, Command('start'))
    dp.message.register(support, F.text == 'Поддержка')
    dp.message.register(add_chat, F.text == 'Добавить новый чат')
    dp.callback_query.register(add_chat, F.data == 'add_chat')
    dp.message.register(user_chats, F.text == 'Мои чаты')
    dp.message.register(handle_message)

    try:
        await dp.start_polling(bot)

    except Exception as e:
        logging.error(e)

    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
