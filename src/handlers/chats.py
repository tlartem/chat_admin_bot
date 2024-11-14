from aiogram import Bot, types
from aiogram.types import ChatMemberUpdated

from config import INVITE_LINK
from keyboards import kb_main_menu
from repository import add_new_chat, get_user_chats


async def add_chat(message: types.Message):
    await message.answer(
        f'Чтобы добавить бота в новый чат, перейдите по [ссылке]({INVITE_LINK}) и выберите чат.',
        parse_mode='Markdown',
    )


async def user_chats(message: types.Message):
    user_chats = await get_user_chats(message.from_user.id)
    if not user_chats:
        await message.answer('У вас нет добавленных чатов.', reply_markup=kb_main_menu)
        return

    await message.answer('Ваши добавленные чаты:')
    for i, chat_id in enumerate(user_chats):
        try:
            chat_info = await message.bot.get_chat(chat_id)
        except Exception as e:
            print(e)
            continue

        chat_info = (
            f"Название чата: {chat_info.title}\n"
            f"Описание: {chat_info.description or 'Без описания'}"
        )
        await message.answer(f'{i+1}. {chat_info}', reply_markup=kb_main_menu)


async def on_bot_added(event: ChatMemberUpdated, bot: Bot):
    if (
        event.new_chat_member.is_chat_member()
        and event.new_chat_member.user.id == bot.id
    ):
        inviter_id = event.from_user.id

        await add_new_chat()

        await bot.send_message(
            inviter_id, 'Спасибо за добавление меня в чат! Я готов к работе.'
        )
