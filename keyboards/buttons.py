from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

directions = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="left 90 "),
            KeyboardButton(text="right 90 "),
        ],

        [
            KeyboardButton(text="forward "),
        ],

    ],
    resize_keyboard=True
)