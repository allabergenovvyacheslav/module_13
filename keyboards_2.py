from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прайс-лист на паркет"),
            KeyboardButton(text="О компании Мир паркета")
        ]
    ], resize_keyboard=True
)