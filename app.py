from loader import bot, storage,db
from aiogram import types, filters
import time
from aiogram import executor
from utils import set_bot_commands



async def on_startup(dp):
    await db.create()
    import filters
    import middlewares
    print('In the startup')
    filters.setup(dp)
    middlewares.setup(dp)


    from utils.notify_admins import on_startup_notify
    await set_bot_commands.set_default_commands(dp)
    await on_startup_notify(dp)

async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
