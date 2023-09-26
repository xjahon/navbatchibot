import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import time

scheduler = AsyncIOScheduler()


@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    # print(users[0][0])
    await message.answer(users)


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text="Bu habar admin tomonidan yuborildi!")
        await asyncio.sleep(0.05)


@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")


@dp.message_handler(text="/mydata")
async def select_data(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    # user = db.select_user(id=message.from_user.id)
    text = f"{user[0]} | {user[1]} | {user[2]} | {user[3]} | {user[4]} | {user[5]}"
    await message.reply(f"{text}")
    # await message.reply(f"{user2[0]}")


# async def auto_send():
#     users = db.select_all_users()
#     for user in users:
#         user_id = user[0]
#         await bot.send_message(chat_id=user_id, text="Bu habar admin tomonidan yuborildi!")
#         await asyncio.sleep(0.05)

# t = time.strftime("02:56:00")
# while True:
#     if time.strftime("%H:%M:%S") == t:
#         print("New code setted")
#         # auto_send()
#         time.sleep(1)
#     else:
#         continue
