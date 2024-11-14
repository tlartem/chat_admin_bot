import asyncio

from aiogram.types import Message

from utils.link_check import extract_urls, link_check
from utils.toxicity_check import check_toxicity


async def handle_message(message: Message):
    toxicity_score = check_toxicity(message.text)
    if toxicity_score > 0.98:
        reply = await message.reply('Токсичное сообщение. Ты ужасен')

        await message.delete()
        await asyncio.sleep(3)
        await reply.delete()

    urls = extract_urls(message.text)
    print(urls)
    if urls:
        for url in urls:
            result = await link_check(url)
            if not result:
                reply = await message.reply('Обнаружена вредная ссылка')

                await message.delete()
                await asyncio.sleep(3)
                await reply.delete()
