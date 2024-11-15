from aiogram import types

from db.repository import add_user_if_not_exists
from keyboards import kb_main_menu, mk_add_chat


async def cmd_start(message: types.Message):
    await add_user_if_not_exists(message.from_user.id, message.from_user.username)
    await message.answer('Добро пожаловать!', reply_markup=kb_main_menu)
    await message.answer('Что хотите сделать?', reply_markup=mk_add_chat)


async def support(message: types.Message):
    await message.answer('Свяжитесь с поддержкой в Telegram: @temiso')
