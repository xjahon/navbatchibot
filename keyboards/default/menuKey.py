from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Menu 🔖'),
            KeyboardButton(text='Sozlamalar ⚙️'),
        ],
    ],
    resize_keyboard=True
)