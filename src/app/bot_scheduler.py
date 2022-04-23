from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from src.DataBase.data_settings import engine
from aiogram import Bot, Dispatcher, executor
import logging
import bot_config
from sqlalchemy import select
from src.DataBase.models import users
from src.app.parser import words_getter
import aioschedule
import asyncio

logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_config.TOKEN)
dp = Dispatcher(bot)


async def send():
    conn = engine.connect()
    s = select([users])
    r = conn.execute(s).fetchall()
    word_list = words_getter()
    for i in range(len(r)):
        await bot.send_message(r[i][2], word_list[i])


async def scheduler():
    aioschedule.every().second.do(send)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(6)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
