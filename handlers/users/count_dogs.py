from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp, db


@dp.message_handler(Command("count"))
async def bot_help(message: types.Message):
    name = message.from_user.full_name
    count = await db.count_dogs()
    await message.answer(
        "\n".join(
            [
                f'Привет, {name}!',
                f'В базе <b>{count}</b> собак',
            ]))