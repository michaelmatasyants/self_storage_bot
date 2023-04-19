import os
from dotenv import load_dotenv
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentTypes

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, ContentTypeFilter
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import Contact

load_dotenv()
tg_token = os.getenv('TG_BOT_TOKEN')
bot = Bot(token=tg_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class D(StatesGroup):
    contact = State()


async def on_startup(_):
    pass


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='*️⃣ Поддержка', callback_data='support'),
        types.InlineKeyboardButton(text='❓ F.A.Q', callback_data='faq'),
        types.InlineKeyboardButton(text='🎒 Забрать вещи', callback_data='get_back'),
        types.InlineKeyboardButton(text='✍ Оставить заявку', callback_data='application'),
        types.InlineKeyboardButton(text='📦 Мои боксы', callback_data='my_boxes'),
    ]
    keyboard.add(*buttons)
    return keyboard


def next_main_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='❌ Отменить', callback_data='cancel'),
        types.InlineKeyboardButton(text='🔧 Забрать курьером', callback_data='by_runner'),
        types.InlineKeyboardButton(text='🚙 Заберу лично', callback_data='by_myself'),
    ]
    keyboard.add(*buttons)
    return keyboard


def giveaway():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='📦 Оставить вещи', callback_data='application'),
        types.InlineKeyboardButton(text='🎒 Забрать вещи', callback_data='get_back')
    ]
    keyboard.add(*buttons)
    return keyboard


def next_keyboard():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='✍ Оставить заявку', callback_data='application'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu'),
    ]
    keyboard.add(*buttons)
    return keyboard


def choose_del():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu'),
        types.InlineKeyboardButton(text='🔧 Позвать курьера', callback_data='runner'),
        types.InlineKeyboardButton(text='🚙 Отвезу сам', callback_data='myself'),
        types.InlineKeyboardButton(text='*️⃣ Поддержка', callback_data='support'),
        types.InlineKeyboardButton(text='❓ F.A.Q', callback_data='faq')
    ]
    keyboard.add(*buttons)
    return keyboard


def request_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('📞 Отправить номер телефона', request_contact=True))
    return keyboard


@dp.callback_query_handler(text='faq')
async def send_faq(call: types.CallbackQuery):
    faq = """
1. Оформите заявку, используя бота.
2. Мы рассчитаем подходящий тариф, исходя из объема вещей.
3. В удобное время к вам приедет команда муверов, упакует вещи, вынесет и отвезёт их на склад или на ваше новое место жительства.
4. Когда какая-то вещь снова понадобится, закажите возврат, и мы привезем её в любую точку Москвы.
5. Наша система не предусматривает дополнительных платежей за неиспользованное пространство. Это означает, \
что вы платите только за тот объем пространства, который фактически занимают ваши вещи, а не за весь объем комнаты для хранения.
6. Мы предлагаем услугу мобильного хранения, которая включает доставку наших профессиональных упаковочных материалов. \
Наша команда муверов соберет, упакует и маркирует все ваши вещи, а затем транспортирует их на наш склад. Все вещи хранятся на отдельных паллетах в надежных условиях. \
Наш склад постоянно контролируется видеокамерами без слепых зон, и круглосуточно охраняется.
7. Вы можете контролировать свои вещи через специальное меню нашего бота. \
Там вы можете заказать возврат вещей в любое удобное для вас время или добавить новые вещи для хранения. \
Все ваши вещи всегда находятся в безопасности и готовы к использованию.
    """
    await call.message.answer(faq, reply_markup=next_keyboard())


@dp.callback_query_handler(text='price')
async def send_price(call: types.CallbackQuery):
    price_list = """
Шины или велосипед: от 749 руб. в месяц
Мало вещей: от 1 490 руб. в месяц
Много вещей: от 8 190 руб. в месяц
Cдача и возврат вещей: бесплатно через терминал или доставка 1 490 р. за 1 м³."""
    await call.message.answer(price_list, reply_markup=next_keyboard())


@dp.callback_query_handler(text='back_to_menu')
async def back_to_menu(call: types.CallbackQuery):
    await call.message.answer(text='Вы вернулись обратно в меню', reply_markup=main_keyboard())


@dp.callback_query_handler(text='application')
async def leave_a_request(call: types.CallbackQuery):
    await call.message.answer('Для продолжения нажмите кнопку ниже', reply_markup=request_keyboard())
    await D.contact.set()


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    text = """Добро пожаловать! 
Мы компания, предоставляющая малогабаритные ячейки для сезонного хранения вещей.
Например велосипеды, каяки, cнегоходы. 
Мы заберём ваши вещи на наш склад, сохраним и привезём обратно в любую точку Москвы.
Для выбора интересующего вас раздела воспользуйтесь кнопками из меню ниже 👇
        """
    await msg.answer(text, reply_markup=main_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=on_startup)