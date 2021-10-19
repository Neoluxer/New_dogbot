from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("add_dog", "Добавить собаку в базу"),
        types.BotCommand("birthday", "Дни рождения"),
        types.BotCommand("br_search", "Поиск пород"),
        types.BotCommand("count", "Подсчет собак"),
    ])
