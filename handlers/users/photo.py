# ﻿from aiogram.types import InputFile
import asyncio
import aioschedule
from Dicts import Dictionaries
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import *
from aiogram import types
from loader import dp, db

SERVER = True


@dp.message_handler()
async def get_message(message: types.Message):
    from loader import bot
    chat_id = message.chat.id

    text = 'Собака не найдена'
    try:

        c = await db.select_all_dogs()
        photo_dict = {}
        breed_dict = {}
        birthday_dict = {}
        weight_dict = {}
        dog_height_dict = {}
        gender_dict = {}
        names_list = []
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=e)

    try:
        if SERVER:

            for items in c:
                photo_dict[items[0].lower()] = items[7]
                breed_dict[items[0].lower()] = items[1]
                birthday_dict[items[0].lower()] = items[3]
                weight_dict[items[0].lower()] = items[2]
                names_list.append(items[0].lower())
                gender_dict[str(items[0]).lower()] = items[9]
                dog_height_dict[str(items[0]).lower()] = items[8]

        else:
            await bot.send_message(chat_id=chat_id, text="no SERVER")
            for items in c:
                photo_dict[items[0].lower()] = items[6]
                breed_dict[items[0].lower()] = items[1]
                birthday_dict[items[0].lower()] = items[3]
                weight_dict[items[0].lower()] = items[2]
                names_list.append(items[0].lower())
                gender_dict[str(items[0]).lower()] = items[9]
                dog_height_dict[str(items[0]).lower()] = items[8]
    except Exception as e:
        await bot.send_message(chat_id=chat_id, text=e)

    requre = message.text
    if requre.lower() in names_list:
        try:
            test_url = photo_dict[requre.lower()]
            bot.send_message(chat_id=chat_id, text=test_url)
        except:
            await bot.send_message(chat_id=chat_id, text="can't do test URL")


    else:
        if SERVER:
            test_url = '/home/pi/Scripts/aiogram-dogbot/PHOTO/no_foto.jpg'
        else:
            test_url = r'PHOTO\no_foto.jpg'

    photo_bytes = InputFile(path_or_bytesio=test_url)

    if requre.lower() in names_list:
        breed = breed_dict[requre.lower()]
        birthday = birthday_dict[requre.lower()]
        weight = weight_dict[requre.lower()]

        gender = gender_dict[requre.lower()]
        dog_height = dog_height_dict[requre.lower()]

        try:
            await bot.send_photo(chat_id=chat_id, photo=photo_bytes)
            await bot.send_message(chat_id=chat_id, text=f'<b>{requre}</b>\n'
                                                         f'<b>Порода</b>: {breed}\n'
                                                         f'<b>День рождения</b>: {birthday}\n'
                                                         f'<b>Вес</b>: {weight} грамм\n'
                                                         f'<b>Гендер</b>: {gender}\n'
                                                         f'<b>Высота в холке</b>: {dog_height} мм\n')
        except:
            await bot.send_message(chat_id=chat_id, text=f'Попробуйте попозже {test_url}')

    else:
        await bot.send_message(chat_id=chat_id, text=text)
