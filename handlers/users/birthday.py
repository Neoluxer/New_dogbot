from aiogram import types, filters
from aiogram.types import InputFile
import datetime
from aiogram.dispatcher.filters import Command
from Dicts import Dictionaries
from loader import dp, db, bot

Holiday = False

holiday_calendar = {'31.12': 'Новый Год',
                    '30.12': 'День Big House',
                    '16.1': 'День Снеговика',
                    '28.2': 'День свечей',
                    '19.3': 'День Меха и Пуха',
                    '4.4': 'День Пранка и мамин День Рождения',
                    '20.5': 'День блина и паштета',
                    '6.6': 'День лени',
                    '11.7': 'День открыток',
                    '1.8': 'День кости',
                    '8.9': 'День работ',
                    '15.10': 'Оранжевый день',
                    '9.1': 'День подарков',
                    '12.3': 'День радости за других собак',
                    }


@dp.message_handler(Command("birthday"))
async def bot_help(message: types.Message):
    global newtext, characteristic_text
    from loader import bot
    chat_id = message.chat.id
    now = datetime.datetime.now()

    split_now_date = f'{now.day}.{now.month}'
    if split_now_date in holiday_calendar:
        Holiday = True
    else:
        Holiday = False

    # Создать список нужных значений
    List_of_dates = []
    part1 = (now.strftime('%d.%m.'))
    #part1 = "01.03."
    for year in range(1995, 2021):
        List_of_dates.append(f'{part1}{year}')
    # print(List_of_dates)
    # Создаем список дней рождений из базы данных
    c = await db.select_all_dogs()
    dict = {}
    characteristic_dict = {}
    photo_dict = {}
    n = 1
    for items in c:
        dict[items[3]] = items[0]
        characteristic_dict[items[0].lower()] = f'Порода: {items[1]}, Вес: {items[2]}, Дата рождения: {items[3]}'
        photo_dict[items[0].lower()] = items[7]

    bad_newstext = 'Сегодня нет дней рождений у собак'
    for items in List_of_dates:
        if items in dict:
            # print (Dictionaries.birthdayas[items])
            birthdays = True

            newtext = (dict[items])
            newtext2 = characteristic_dict
            namew = dict[items]
            low_namew = namew.lower()
            characteristic_text = (newtext2[low_namew])
            break
    else:
        birthdays = False
        test_url = '/home/pi/Scripts/aiogram-dogbot/PHOTO/no_foto.jpg'
        low_namew = 'no name'

    if low_namew in photo_dict:
        test_url = photo_dict[low_namew.lower()]
    else:
        test_url = '/home/pi/Scripts/aiogram-dogbot/PHOTO/no_foto.jpg'

    photo_bytes = InputFile(path_or_bytesio=test_url)
    # photo_bytes = InputFile(
    #     path_or_bytesio="C:\\Users\\Professional\\PycharmProjects\\aiogram-dogbot\\PHOTO\\khachane\\IMG_3451.JPG")

    text = [
        'Список дней рождений: ',

    ]
    if Holiday:
        holiday_text = holiday_calendar[split_now_date]
    else:
        holiday_text = 'Нет дня рождения'

    await message.answer('\n'.join(text))
    full_list_of_today_birthdays = []
    if birthdays:
        for k in sorted(dict.keys()):
            a = str(k)
            b = ('.'.join(a.split('.')[:-1]))
            c = f'{b}.'
            if c == part1:
                full_list_of_today_birthdays.append(dict[k])

        if (len(full_list_of_today_birthdays) == 2):
            namew1 = full_list_of_today_birthdays[0]
            low_namew1 = namew1.lower()
            namew2 = full_list_of_today_birthdays[1]
            low_namew2 = namew2.lower()
            characteristic_text2 = (f"<b>{namew1.upper()}</b>\n{characteristic_dict[low_namew1]}")
            characteristic_text3 = (f"<b>{namew2.upper()}</b>\n{characteristic_dict[low_namew2]}")


            test_url1 = photo_dict[low_namew1.lower()]
            test_url2 = photo_dict[low_namew2.lower()]
            # test_url1 = "C:\\Users\\Professional\\PycharmProjects\\aiogram-dogbot\\PHOTO\\khachane\\IMG_3451.JPG"
            # test_url2 = "C:\\Users\\Professional\\PycharmProjects\\aiogram-dogbot\\PHOTO\\khachane\\IMG_3451.JPG"
            photo_bytes1 = InputFile(
                path_or_bytesio=test_url1)
            photo_bytes2 = InputFile(
                path_or_bytesio=test_url2)
            try:
                await message.answer(text=characteristic_text2.capitalize())
                await bot.send_photo(chat_id=chat_id, photo=photo_bytes1)
                await message.answer(text=characteristic_text3.capitalize())
                await bot.send_photo(chat_id=chat_id, photo=photo_bytes2)
            except Exception as e:
                print(test_url)
                await message.answer(test_url1)
                await message.answer(test_url2)


        if (len(full_list_of_today_birthdays) == 3):
            namew1 = full_list_of_today_birthdays[0]
            low_namew1 = namew1.lower()
            namew2 = full_list_of_today_birthdays[1]
            low_namew2 = namew2.lower()
            namew3 = full_list_of_today_birthdays[2]
            low_namew3 = namew3.lower()
            characteristic_text2 = (f"<b>{namew1.upper()}</b>\n{characteristic_dict[low_namew1]}")
            characteristic_text3 = (f"<b>{namew2.upper()}</b>\n{characteristic_dict[low_namew2]}")
            characteristic_text4 = (f"<b>{namew3.upper()}</b>\n{characteristic_dict[low_namew3]}")
            await message.answer(text=characteristic_text2.capitalize())
            await message.answer(text=characteristic_text3.capitalize())
            await message.answer(text=characteristic_text4.capitalize())
            test_url1 = photo_dict[low_namew1.lower()]
            test_url2 = photo_dict[low_namew2.lower()]
            test_url3 = photo_dict[low_namew3.lower()]
            photo_bytes1 = InputFile(
                path_or_bytesio=test_url1)
            photo_bytes2 = InputFile(
                path_or_bytesio=test_url2)
            photo_bytes3 = InputFile(
                path_or_bytesio=test_url3)
            try:
                await bot.send_photo(chat_id=chat_id, photo=photo_bytes1)
                await bot.send_photo(chat_id=chat_id, photo=photo_bytes2)
                await bot.send_photo(chat_id=chat_id, photo=photo_bytes3)
            except Exception as e:
                print(test_url)
                await message.answer(test_url1)
                await message.answer(test_url2)
                await message.answer(test_url3)

        if (len(full_list_of_today_birthdays) == 1):
            await message.answer(text=newtext.capitalize())
            await message.answer(text=characteristic_text.capitalize())

            try:
                await bot.send_photo(chat_id=chat_id, photo=photo_bytes)
            except Exception as e:
                print(test_url)
                await message.answer(test_url)
                await message.answer(str(e))

    else:
        await message.answer(text=bad_newstext)

    if Holiday:
        try:
            await message.answer(text='Сегодня праздник!')
            await message.answer(text=str(holiday_text))
        except Exception as e:
            await message.answer(text=str(e))


    else:
        await message.answer(text='Сегодня нет праздников.')
