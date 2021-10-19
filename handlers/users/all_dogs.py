# -*- coding: utf-8 -*-

from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp, db


@dp.message_handler(Command('all_dogs'))
async def dog_preview(message: types.Message):

    c = await db.select_all_dogs()

    dict = []
    n=1
    for items in c:
        dict.append(f'<b>{items[0]} </b>: ({items[1]})')
        n += 1

    await message.answer(dict[0:20])
    await message.answer(dict[20:40])
    await message.answer(dict[40:80])
    await message.answer(dict[80:100])
    await message.answer(dict[100:120])
    await message.answer(dict[120:140])
    await message.answer(dict[140:160])
    await message.answer(dict[160:180])
    await message.answer(dict[180:200])
    await message.answer(dict[200:-1])

