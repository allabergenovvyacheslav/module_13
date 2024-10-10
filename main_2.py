import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from config_2 import *
from keyboards_2 import *
import texts_2

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(texts_2.start, reply_markup=start_kb)

@dp.message_handler(text="О компании Мир паркета")
async def inform(message):
    await message.answer(texts_2.about, reply_markup=start_kb)

@dp.message_handler(text="Цены")
async def price(message):
    await message.answer("Выберите позицию из прайса", catalog_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)