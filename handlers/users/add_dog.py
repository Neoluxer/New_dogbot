from aiogram import types, filters
import datetime
import os
from aiogram.types import ContentType, Message
from loader import dp, db, bot
from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.buttons import gender
from states import Dogs
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from Classes.open_file_2 import Dog
from datetime import timedelta, datetime
import configuration

try:
    import pickle5 as pickle
except:
    import pickle


@dp.message_handler(Command('add_dog'))
async def enter_article_creation(message: types.Message):
    await message.answer("Имя собаки: ")
    await Dogs.next()


@dp.message_handler(state=Dogs.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data["answer"] = answer
    await message.answer("Вес собаки: ")
    await Dogs.next()


@dp.message_handler(state=Dogs.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer2 = message.text
    async with state.proxy() as data:
        data["answer2"] = answer2
    await message.answer("Порода собаки: ")
    await Dogs.next()


@dp.message_handler(state=Dogs.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer3 = message.text
    async with state.proxy() as data:
        data["answer3"] = answer3
    await message.answer("Возраст собаки (годы): ")
    await Dogs.next()


@dp.message_handler(state=Dogs.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer4 = message.text
    async with state.proxy() as data:
        data["answer4"] = answer4
    await message.answer("Возраст собаки (месяцы): ")
    await Dogs.next()


@dp.message_handler(state=Dogs.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer5 = message.text
    async with state.proxy() as data:
        data["answer5"] = answer5
    await message.answer("Возраст собаки (дни): ")
    await Dogs.next()



@dp.message_handler(state=Dogs.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    print ("here")
    answer6 = message.text
    print(answer6)
    async with state.proxy() as data:
        data["answer6"] = answer6  # Записываем возраст собаки
    await message.answer("Высота собаки (мм): ")
    await Dogs.next()


@dp.message_handler(state=Dogs.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer7 = message.text  # Высота собаки
    async with state.proxy() as data:
        data["answer7"] = answer7 # Высота собаки
    await message.answer("Гендер: ", reply_markup=gender)
    await Dogs.next()

@dp.message_handler(state=Dogs.Q8)
async def answer_q8(message: types.Message, state: FSMContext):
    answer8 = message.text
    async with state.proxy() as data:
        data["answer8"] = answer8  # Гендер
    await message.answer("Фото: ")
    await Dogs.next()


@dp.message_handler(content_types=ContentType.PHOTO, state=Dogs.Q9)
async def answer_q9(message: types.Message, state: FSMContext):
    answer9 = message.photo[-1].file_id  # фотография
    print(answer9)
    async with state.proxy() as data:

        answer = data.get("answer")  # имя собаки
        answer2 = data.get("answer2")  # вес собаки
        answer3 = data.get("answer3")  # порода собаки
        answer4 = data.get("answer4")  # годы
        answer5 = data.get("answer5")  # месяцы
        answer6 = data.get("answer6")  # дни
        answer7 = data.get("answer7")  # высота собаки
        answer8 = data.get("answer8")  # гендер

        days = (int(answer4) * 365) + (int(answer5) * 30) + int(answer6)

        delta = timedelta(days)
        today = datetime.now()
        date2 = today - delta
        date = str(date2.strftime('%d.%m.%Y'))

        new_dog = Dog(name=answer, breed=answer3, weight=answer2, age=date)
        if configuration.SERVER:
            picture_path = f'/home/pi/Scripts/aiogram-dogbot/PHOTO/{new_dog.latinica()}/{new_dog.latinica()}.JPG'  # todo Этот путь надо будет переделать когда подключу Raspberry Pie
            picture_link = f'https://www.neoluxe.ru/photo/{new_dog.latinica()}/{new_dog.latinica()}.JPG'  # todo Этот путь надо будет переделать когда подключу Raspberry Pie
        else:
            picture_path = f'PHOTO\\{new_dog.latinica()}\\{new_dog.latinica()}.JPG'
            picture_link = f'https://www.neoluxe.ru/photo/{new_dog.latinica()}/{new_dog.latinica()}.JPG'

        file_info = await bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = await bot.download_file(file_info.file_path)
        if configuration.SERVER:
            path = f'/home/pi/Scripts/aiogram-dogbot/PHOTO/{new_dog.latinica()}/'
        else:
            path = f'PHOTO\\{new_dog.latinica()}\\'

        try:
            os.mkdir(path)
        except OSError:
            print("Создать директорию %s не удалось" % path)
        else:
            print("Успешно создана директория %s " % path)
        if configuration.SERVER:
            src = f'/home/pi/Scripts/aiogram-dogbot/PHOTO/{new_dog.latinica()}/{new_dog.latinica()}.JPG'
        else:
            src = f'PHOTO\\{new_dog.latinica()}\\{new_dog.latinica()}.JPG'

        try:
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file.getvalue())

            await message.answer(f"Картинка сохранена в папку{src}", reply_markup=ReplyKeyboardRemove())
        except Exception as e:
            print(e)
            await message.answer("Картинку сохранить не удалось")
            await Dogs.previous()
        src_alter = f'PHOTO\\{new_dog.latinica()}\\{new_dog.latinica()}.JPG'
    try:
        await db.add_dogs(naming=answer, weight=float(answer2), breed=answer3, link=new_dog.latinica(),
                          birthday=str(date), picture_path=src_alter, picture_link=src, gender=answer8, dog_height=int(answer7))
        if configuration.SERVER:
            way = f'/home/pi/Scripts/aiogram-dogbot/BIN/{new_dog.latinica()}.bin'
        else:
            way = f'BIN\\{new_dog.latinica()}.bin'

        with open(way, "wb") as f:
            pickle.dump(new_dog, f, protocol=pickle.HIGHEST_PROTOCOL)
        print('Файл перезаписан')

        await message.answer("Запись в базу данных удалась!")
        await state.finish()
    except Exception as e:
        print(e)
        print('Запись в базу данных не удалась')
        breakpoint()
        await Dogs.previous()
