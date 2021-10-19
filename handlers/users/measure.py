from aiogram.dispatcher.filters import Command
from loader import dp, bot, db
from aiogram import types
from Classes.Pycairo import PycairoPaint
from states import Measuring
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile

All_is_good = False


@dp.message_handler(Command('measure'))
async def measure(message: types.Message):
    await message.answer("Вы начали вносить результаты замеров.\n"
                         "Введите данные в формате (left 90 forward 2000 right 87 forward 300: ")
    await Measuring.first()


@dp.message_handler(state=Measuring.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    global All_is_good
    All_is_good = False
    global list_oaf_all_directions
    answer = message.text  # Сюда пришли все данные по замерам
    try:
        c = await db.select_all_dictionary()
        await message.answer(f'подключение к базе данных удалось')
    except Exception as e:
        await message.answer(f'{e}')
        await state.reset_state(with_data=True)

    list_of_direction_left = []
    list_of_direction_right = []
    list_of_direction_forward = []
    list_of_starts =[]
    try:
        for items in c:
            list_of_direction_left.append(items[0])
            list_of_direction_right.append(items[1])
            list_of_direction_forward.append(items[2])
            list_of_starts.append(items[3])
            list_oaf_all_directions = list_of_direction_right + list_of_direction_left + list_of_direction_forward + list_of_starts
            # Формируется словарь с допустимыми командами из соответствующей базы данных

            # await message.answer(f'Создать список удалось!\n'
            #                      f'{str(list_oaf_all_directions)}')
    except Exception as e:
        await message.answer(f'{e}')
        await state.reset_state(with_data=True)

    await message.answer(f"Вы начали вносить {answer}.\n")
    new_class_exemplyar = PycairoPaint(measure=answer)
    async with state.proxy() as data:
        data["answer"] = answer  # В память записываются координаты
    split_a = answer.split(" ")
    for items in split_a:
        if items not in list_oaf_all_directions and items.isdigit() == False:
            await message.answer(f'{items} Не в списке')
            await Measuring.previous()
            All_is_good = False
        else:
            All_is_good = True

    await message.answer("Введите название файла (new_file):")
    await Measuring.next()

@dp.message_handler(state=Measuring.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer3 = message.text
    async with state.proxy() as data:
        coordinates = data.get("answer")  # Достаем записанные ф файл координаты

    try:
        chat_id = message.chat.id
        await message.answer(coordinates)
        new_picture = PycairoPaint(measure=coordinates, path=answer3)
        new_picture.Drawing()
        new_picture.FinishDrawing()
        if All_is_good:
            photo_bytes = InputFile(path_or_bytesio=f'/home/pi/Scripts/aiogram-dogbot/PHOTO/{answer3}.png')
            await bot.send_photo(chat_id=chat_id, photo=photo_bytes)
            await message.answer('Задача выполнена успешно')
            await state.finish()
        else:
            await message.answer('ведены неверные команды')
            await state.finish()

    except Exception as e:
        await message.answer(str(e))
        await state.finish()


        # todo Нужно записывать результаты в новое место или чистить лист
