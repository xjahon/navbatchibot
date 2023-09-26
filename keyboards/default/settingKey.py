from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

setting = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🔄 Guruhni o`zgartirish'),
        ],
        [
            KeyboardButton(text='⬅️ Ortga'),
        ]
    ],
    resize_keyboard=True
)