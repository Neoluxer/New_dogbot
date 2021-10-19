from aiogram.types import InputFile
import asyncio
import aioschedule
from Dicts import Dictionaries
from aiogram.dispatcher.filters.builtin import Text
from aiogram import types
from loader import dp,db


@dp.message_handler()
async def get_message(message: types.Message):

    from loader import bot
    chat_id = message.chat.id
    text = 'Собака не найдена дог бот сломался'
    c = await db.select_all_dogs()
    photo_dict = {}
    breed_dict ={}
    birthday_dict={}
    weight_dict={}
    names_list=[]
    for items in c:
        photo_dict[items[0].lower()] = items[7]
        breed_dict[items[0].lower()] = items[1]
        birthday_dict[items[0].lower()] = items[3]
        weight_dict[items[0].lower()] = items[2]
        names_list.append(items[0].lower())

    requre = message.text
    if requre.lower() in names_list:
        test_url = photo_dict[requre.lower()]

    else:
        test_url ='/home/pi/Scripts/aiogram-dogbot/PHOTO/no_foto.jpg'
    photo_bytes = InputFile(path_or_bytesio=test_url)


    if requre.lower() in names_list:
        breed = breed_dict[requre.lower()]
        birthday = birthday_dict[requre.lower()]
        weight = weight_dict[requre.lower()]
        try:
            await bot.send_photo(chat_id=chat_id, photo=photo_bytes)
            await bot.send_message(chat_id=chat_id, text=f'<b>{requre}</b>\n{breed}\n{birthday}\n{weight}')
        except:
            await bot.send_message(chat_id=chat_id, text=f'Попробуйте попозже {test_url}')

    else:
        await bot.send_message(chat_id=chat_id, text=text)
