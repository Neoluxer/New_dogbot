from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/add_dog - Ввести собаку',
        '/birthday - День рождения собаки',
        '/all_dogs - Посмотреть всех собак',
        '/count - Посчитать всех собак',
        '/br_search - Поиск породы',

    ]
    await message.answer('\n'.join(text))
