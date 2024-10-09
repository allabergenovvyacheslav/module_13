"""
Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot.

Задача "Ещё больше выбора":

Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать'
присылалась Inline-клавиатруа.

Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'

Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'

Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.

Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.

По итогу получится следующий алгоритм:
Вводится команда /start
На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и
'Формулы расчёта'
По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    gender = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    button_1 = KeyboardButton(text='Рассчитать')
    button_2 = KeyboardButton(text='Информация')
    keyboard_1 = ReplyKeyboardMarkup(
        resize_keyboard=True,
        input_field_placeholder='Введите данные здесь')
    keyboard_1.add(button_1)
    keyboard_1.add(button_2)
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard_1)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer(
        'Этот бот помогает рассчитать сколько вам необходимо потреблять ежедневно калорий.'
    )


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
    button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    keyboard_2: InlineKeyboardMarkup = InlineKeyboardMarkup()
    keyboard_2.add(button_3)
    keyboard_2.add(button_4)
    await message.answer('Выберите опцию:', reply_markup=keyboard_2)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; '
                              'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_gender(call):
    await call.message.answer('Назовите свой пол: men/women')
    await UserState.gender.set()


@dp.message_handler(state=UserState.gender)
async def set_age(message, state):
    await state.update_data(gender=message.text.lower())
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    if data['gender'] == 'women':
        res_for_women = (
                10 * data['weight']
                + 6.25 * data['growth']
                - 5 * data['age']
                - 161
        )
        await message.answer(f'Ваша норма калорий {res_for_women}')
    if data['gender'] == 'men':
        res_for_men = (
                10 * data['weight']
                + 6.25 * data['growth']
                - 5 * data['age']
                + 5
        )
        await message.answer(f'Ваша норма калорий {res_for_men}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
