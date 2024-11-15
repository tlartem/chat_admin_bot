from aiogram import types

from config import INVITE_LINK
from db.repository import ChatRepo
from keyboards import kb_main_menu


async def add_chat(message: types.Message):
    await message.answer(
        f'Чтобы добавить бота в новый чат, перейдите по [ссылке]({INVITE_LINK}) и выберите чат.',
        parse_mode='Markdown',
    )


async def user_chats(message: types.Message):
    chat_repo = ChatRepo(None)

    user_chats = await chat_repo.find_chats_by_user(message.from_user.id)
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
