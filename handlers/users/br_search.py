from aiogram import types, filters
import datetime
from aiogram.dispatcher.filters import Command
from loader import dp, db, bot
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from states import BrSearch
from aiogram.dispatcher import FSMContext


@dp.message_handler(Command("br_search"))
async def bot_help(message: types.Message):
    from loader import bot
    chat_id = message.chat.id
    now = datetime.datetime.now()
    await message.answer("Порода собаки: ")
    await BrSearch.next()


@dp.message_handler(state=BrSearch.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    c = await db.select_all_dogs()
    dict = {}
    breed_dict = {}
    characteristic_dict = {}
    breed_list = []
    for items in c:
        dict[items[3]] = items[0]  # Словарь ИМЯ:ДЕНЬ РОЖДЕНИЯ
        breed_dict[items[1]] = items[0]  # Словарь ИМЯ:ПОРОДА
        breed_list.append(items[1])
        characteristic_dict[items[0].lower()] = f'Порода: {items[1]}, Вес: {items[2]}, Дата рождения: {items[3]}'

    breed_input = message.text
    d = process.extractOne(breed_input, breed_list)


    dict = []
    n = 1
    for items in c:
        if items[1]==d[0]:
            dict.append(f'<b>{items[0]} </b>: ({items[1]})')
            n += 1

    await message.answer(str(dict[0:20]))



    # for items in breed_dict:
    #
    #     if items == d[0]:
    #         new_text = (breed_dict[items[0]])
    #         searching_breed_list[new_text] = items[0]
    #
    # keys = searching_breed_list.keys()
    # await message.answer('test')
    #
    #
    # for values in keys:
    #     await message.answer(
    #         "\n".join(
    #             [
    #                 f'<b>{values}</b>',
    #
    #             ]))
    await state.finish()
