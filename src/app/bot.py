from src.DataBase.data_settings import engine
from src.DataBase.models import users
from aiogram import Bot, Dispatcher, executor, types
from telegram import get_participants
from sqlalchemy import select
from src.app.parser import words_getter
import aioschedule
import asyncio
import bot_config
import logging


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if '/start' in message.text:
        participants = await get_participants('https://t.me/TestGoup74')
        user_ids = [p['user_id'] for p in participants]

        if message.from_user.id in user_ids:
            await message.answer('Добро пожаловать в Золотое яблоко!')
            ins = users.insert().values(
                username=message.from_user.username,
                user_id=message.from_user.id,
                first_name=message.from_user.first_name
            )
            conn = engine.connect()
            r = conn.execute(ins)

        else:
            await message.answer('К сожалению, у вас недостаточно прав на использование этого бота. Обратитесь к '
                                 'системному администратору')


@dp.message_handler(commands='stop')
async def stop(message: types.Message):
    if '/stop' in message.text:
        await message.answer('До свидания! С наилучшими пожеланиями, Золотое Яблоко')


async def send():
    conn = engine.connect()
    s = select([users])
    r = conn.execute(s).fetchall()
    word_list = words_getter()
    for i in range(len(r)):
        await bot.send_message(r[i][2], word_list[i])


async def scheduler():
    aioschedule.every().day.at('14:00').do(send)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
