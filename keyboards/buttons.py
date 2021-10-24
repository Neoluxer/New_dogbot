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

gender = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="сука"),
            KeyboardButton(text="кобель"),
        ],

        [
            KeyboardButton(text="небинарный"),
        ],

    ],
    resize_keyboard=True
)
