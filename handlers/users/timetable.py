from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from Test.testJSON import func
from loader import dp, db
from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Tashkent')
date = datetime.now(IST)
# date.strftime('%a')
kun = date.strftime('%a')

week = {
    'Mon': "Dushanba",
    'Tue': "Seshanba ",
    'Wed': "Chorshanba",
    'Thu': "Payshanba",
    'Fri': "Juma",
    'Sat': "Shanba",
}
# autoSend = date.strftime()


@dp.message_handler(Command("timetable"))
async def bot_help(message: types.Message):
    user = db.select_user(id=message.from_user.id)
    # print(user)
    guruh = user[5].upper()
    text = func(user[3], user[4], user[5], kun)
    await message.answer(f" {date.strftime('%d.%m.%Y')} \t\t\t\t{week[kun]}  \n<b>Gruppa: \t\t\t\t</b> {guruh} \n\n{text}", disable_web_page_preview=True)
    # await message.answer(f"Salom {user[2]}")

# @dp.callback_query_handler()
# async def get_group(call: types.CallbackQuery):
#     callback_data = call.data
