# import pytz
# from datetime import datetime
# from loader import dp, db
# from Test.kv import func
# import asyncio
# from loader import dp, db, bot
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from datetime import datetime

# scheduler = AsyncIOScheduler()
# scheduler.start()


# IST = pytz.timezone('Asia/Tashkent')
# date = datetime.now(IST)
# # date.strftime('%a')
# kun = date.strftime('%a')

# week = {
#     'Mon': "Dushanba",
#     'Tue': "Seshanba ",
#     'Wed': "Chorshanba",
#     'Thu': "Payshanba",
#     'Fri': "Juma",
#     'Sat': "Shanba",
# }


# async def send_message_to_admin():
#     users = db.select_all_users()
#     for user in users:
#         guruh = user[5].upper()
#         text = func(user[3], user[4], user[5], datetime.today().strftime('%a'))
#         my_msg = f" {datetime.today().strftime('%d.%m.%Y')} | {datetime.now().strftime('%H:%M:%S')} \t\t\t\t{week[datetime.today().strftime('%a')]}  \n<b>Gruppa: \t\t\t\t</b> {guruh} \n\n{text}"
#         # my_msg = f" {}"
#         user_id = user[0]
#         await bot.send_message(text=my_msg, chat_id=user_id, disable_web_page_preview=True)
#         await asyncio.sleep(0.05)

# scheduler.add_job(send_message_to_admin, "interval", minutes=1)
