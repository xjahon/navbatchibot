import pytz
from datetime import datetime
from loader import dp, db
from Test.kv import func
import asyncio
from loader import dp, db, bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

scheduler = AsyncIOScheduler()
scheduler.start()


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
async def send_message():
        text = func(datetime.today().strftime('%a'))
        my_msg = f" {datetime.today().strftime('%d.%m.%Y')} | {datetime.now().strftime('%H:%M:%S')} \t\t\t\t{week[datetime.today().strftime('%a')]}  \n<b>Navbatchi: \t\t\t\t</b> \n\n{text}"
        # my_msg = "hgvgkjv"
        await bot.send_message(chat_id="@navbatchi74326", text=text)
        await asyncio.sleep(0.05)

scheduler.add_job(send_message, "interval", minutes=1)
