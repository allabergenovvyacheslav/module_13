import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
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


@dp.message_handler(text="Прайс-лист на паркет")
async def price(message):
    await message.answer("Выберите позицию из прайса", reply_markup=catalog_kb)


@dp.callback_query_handler(text="parquet_flooring_S")
async def buy_parquet_flooring_S(call):
    await call.message.answer(texts_2.parquet_flooring_S, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="large_format_parquet_S")
async def buy_large_format_parquet_S(call):
    await call.message.answer(texts_2.large_format_parquet_S, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="solid_wood_parquet_S")
async def buy_solid_wood_parquet_S(call):
    await call.message.answer(texts_2.solid_wood_parquet_S, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="parquet_flooring_N")
async def buy_parquet_flooring_N(call):
    await call.message.answer(texts_2.parquet_flooring_N, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="large_format_parquet_N")
async def buy_large_format_parquet_N(call):
    await call.message.answer(texts_2.large_format_parquet_N, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="solid_wood_parquet_N")
async def buy_solid_wood_parquet_N(call):
    await call.message.answer(texts_2.solid_wood_parquet_N, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="parquet_flooring_R")
async def buy_parquet_flooring_R(call):
    await call.message.answer(texts_2.parquet_flooring_R, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="large_format_parquet_R")
async def buy_large_format_parquet_R(call):
    await call.message.answer(texts_2.large_format_parquet_R, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="solid_wood_parquet_R")
async def buy_solid_wood_parquet_R(call):
    await call.message.answer(texts_2.solid_wood_parquet_R, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="oter")
async def buy_oter(call):
    await call.message.answer(texts_2.oter)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
