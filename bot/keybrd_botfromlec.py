from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость"),
            KeyboardButton(text="О нас")
        ]
    ], resize_keyboard=True
)


catalog_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Средняя Игра", callback_data="medium")],
        [InlineKeyboardButton(text="Большая Игра", callback_data="big")],
        [InlineKeyboardButton(text="Очень большая игра", callback_data="mega")],
        [InlineKeyboardButton(text="Другие предложения", callback_data="other")]
    ]
)


b_kb = InlineKeyboardMarkup(
    Inline_Keyboard=[
        [InlineKeyboardButton(text="Купить!", url="https://ya.ru")]
    ]
)
