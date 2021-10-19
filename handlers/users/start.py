import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loguru import logger
from loader import dp
# from keyboards.menu import start_menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Добрый день, {message.from_user.full_name}')
    name = message.from_user.full_name

