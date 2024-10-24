import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions


logging.basicConfig(level=logging.INFO)


api = '7774312557:AAFXxYlW-qQu-Kz05nU4_AQ4-vhaAc6LE9I'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
button_0 = KeyboardButton(text='Регистрация')
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
kb1.add(button_0)
kb1.add(button_1)
kb1.add(button_2)
kb1.add(button_3)


kb_in1 = InlineKeyboardMarkup()
button_3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in1.add(button_3)
kb_in1.add(button_4)


kb_in2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Продукт 1', callback_data='product_buying',),
            InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
            InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
        ]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer('Добро пожаловать!', reply_markup=kb1)


@dp.message_handler(text=['Регистрация'])
async def sign_up(message):
    await message.answer("Введите имя пользователя на русском:", reply_markup=kb1)
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    user_included = crud_functions.is_included(message.text)
    if user_included:
        await message.answer('Пользователь существует, измените имя', reply_markup=kb1)
        await RegistrationState.username.set()
        return
    await state.update_data(username=message.text)
    await message.answer("Введите свой email")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите возраст", reply_markup=kb1)
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'], 1000)
    await message.answer(f'Регистрация прошла успешно', reply_markup=kb1)
    await state.finish()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in1)


@dp.message_handler(text="Информация")
async def info(message):
    about = "Мы продаем лучшие продукты, попробуйте сами"
    with open("img/about.webp", "rb") as img1:
        await message.answer_photo(img1, about, reply_markup=kb1)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;'
                              '\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 4.92 * int(data['age']) - 161
    await message.answer(f'Ваша норма калорий {result}', reply_markup=kb1)
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for index, product in enumerate(crud_functions.get_all_products()):
        await message.answer(f"Название:{product[1]} | Описание:{product[2]} | Цена: {product[3]}")
        with open(f'img/product {index + 1}.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await message.answer("Выберите продукт для покупки:", reply_markup=kb_in2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
