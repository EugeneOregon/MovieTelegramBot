import asyncio

from aiogram import executor

# Do not delete
import middlewares
import filters
import handlers

from loader import dp, db
from models.main import Check
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Default commands
    await set_default_commands(dispatcher)
    # Starting the database
    await db.create()
    await db.create_table_films()
    # Administrator notice
    await on_startup_notify(dispatcher)


# Event Scheduler
async def scheduled(wait_time):
    while True:
        await asyncio.sleep(wait_time)
        check = Check()
        await check.check_movie_in_db()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Specify with what interval to do the check
    loop.create_task(scheduled(3600))
    executor.start_polling(dp, on_startup=on_startup)
