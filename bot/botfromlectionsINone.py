from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging


# ______________________________________config

api = "7774312557:AAFXxYlW-qQu-Kz05nU4_AQ4-vhaAc6LE9I"

# price of game

priceM = 1500
priceL = 2000
priceXL = 3000

# _____________________________________end_config


logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# ______________________________________text
start1 = "Рады вас приветствовать в магазине настольных игр."

about = "Мы продаем лучшие игры уже 2000 лет, но вы нам не поверите, поэтому скажем что два дня"

Mgame = f' Лучший вариант для начинающих, игра небольшого размера. Стоимость {priceM} руб.'

Lgame = f'Альтернатива для тех, кто не знает, что выбрать. Стоимость {priceL} руб.'

XLgame = f'Лучший комплект для игромана, игра плюс бонусные материалы по ней.  Стоимость {priceXL} руб. '

other = "Вы хотите что-то другое, обратитесь к админу @MegaAdminNastolokRU."

qw = "Что вас интересует?"
# ____________________________________end text
# ________________________________keyboard
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость"),
            KeyboardButton(text="О нас")
        ]
    ], resize_keyboard=True
)
# ________________________________end_keyboard


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(start1, reply_markup=start_kb)


@dp.message_handler(text="О нас")
async def info(message):
    await message.answer(about, reply_markup=start_kb)


# ________________________________keyboard
catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text= "Средняя Игра", callback_data= "medium")],
        [InlineKeyboardButton(text= "Большая Игра", callback_data= "big")],
        [InlineKeyboardButton(text= "Очень большая игра", callback_data= "mega")],
        [InlineKeyboardButton(text= "Другие предложения", callback_data= "other")]
    ]
)
# ________________________________end_keyboard
@dp.message_handler(text="Стоимость")
async def price(message):
    await message.answer(qw, reply_markup=catalog_kb)


# ________________________________keyboard
buy_kb = InlineKeyboardMarkup(
    inline_Keyboard=[
        [InlineKeyboardButton(text = "Купить!", url = "https://ya.ru/?npr=1")]

    ]
)
# ________________________________end_keyboard


@dp.callback_query_handler(text="medium")
async def buy_m(call):
    await call.message.answer(Mgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="big")
async def buy_l(call):
    await call.message.answer(Lgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="mega")
async def buy_xl(call):
    await call.message.answer(XLgame, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="other")
async def buy_other(call):
    await call.message.answer(other, reply_markup=buy_kb)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
