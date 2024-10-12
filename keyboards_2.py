from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Прайс-лист на паркет"),
            KeyboardButton(text="О компании Мир паркета")
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Штучный паркет дуб селект", callback_data='parquet_flooring_S')],
        [InlineKeyboardButton(text="Широкоформатный паркет дуб селект", callback_data='large_format_parquet_S')],
        [InlineKeyboardButton(text="Массивная доска дуб селект", callback_data='solid_wood_parquet_S')],
        [InlineKeyboardButton(text="Штучный паркет дуб натур", callback_data='parquet_flooring_N')],
        [InlineKeyboardButton(text="Широкоформатный паркет дуб натур", callback_data='large_format_parquet_N')],
        [InlineKeyboardButton(text="Массивная доска дуб натур", callback_data='solid_wood_parquet_N')],
        [InlineKeyboardButton(text="Штучный паркет дуб рустик", callback_data='parquet_flooring_R')],
        [InlineKeyboardButton(text="Широкоформатный паркет дуб рустик", callback_data='large_format_parquet_R')],
        [InlineKeyboardButton(text="Массивная доска дуб рустик", callback_data='solid_wood_parquet_R')],
        [InlineKeyboardButton(text="Другие предложения", callback_data='oter')]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить', url='http://mir-parketa.spb.ru')]
    ]
)
