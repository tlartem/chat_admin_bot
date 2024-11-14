from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

kb_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Мои чаты'),
        ],
        [
            KeyboardButton(text='Добавить новый чат'),
            KeyboardButton(text='Поддержка'),
        ],
    ],
)

mk_add_chat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Добавить новый чат',
                callback_data='add_chat',
            ),
        ],
    ]
)
