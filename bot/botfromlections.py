from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
from config_botfromlec import *
from keybrd_botfromlec import *
import text_botfromlec

logging.basicConfig(level=logging.INFO)
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(text_botfromlec.start, reply_markup=start_kb)


@dp.message_handler(text = "О нас")
async def info(message):
    await message.answer(text_botfromlec.about, reply_markup=start_kb)


@dp.message_handler(text = "Стоимость")
async def price(message):
    await message.answer(text_botfromlec.qw, reply_markup=catalog_kb1)


@dp.callback_query_handler(text = "medium")
async def buy_m(call):
    await call.message.answer(text_botfromlec.Mgame, reply_markup=b_kb)
    await call.answer()


@dp.callback_query_handler(text = "big")
async def buy_l(call):
    await call.message.answer(text_botfromlec.Lgame, reply_markup=b_kb)
    await call.answer()


@dp.callback_query_handler(text = "mega")
async def buy_xl(call):
    await call.message.answer(text_botfromlec.XLgame, reply_markup=b_kb)
    await call.answer()


@dp.callback_query_handler(text = "other")
async def buy_other(call):
    await call.message.answer(text_botfromlec.other, reply_markup=b_kb)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
