import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKey import menu

from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    full_name = message.from_user.full_name
    username = message.from_user.username
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    full_name=full_name,
                    username=username)
        await message.answer("Xush kelibsiz!")
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    except sqlite3.IntegrityError as err:
        # await bot.send_message(chat_id=ADMINS[0], text=err)
        await message.answer("Siz ro'yhatdan o'tgansiz!\nBotni yangilash uchun /restart buyrug'ini bosing")
