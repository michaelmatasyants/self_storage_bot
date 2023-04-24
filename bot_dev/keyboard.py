from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatActions, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types


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


def support_buttons():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='📩 Обратиться в поддержу', callback_data='letter_to_sup'),
        types.InlineKeyboardButton(text='🎒 Забрать вещи', callback_data='get_back'),
        types.InlineKeyboardButton(text='📦 Мои боксы', callback_data='my_boxes'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
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


def storage_list():
    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='✅ Что можно хранить на складе', callback_data='storage_list'),
        types.InlineKeyboardButton(text='✍ Оставить заявку', callback_data='application'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')

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
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('📞 Отправить номер телефона',
                                                                            request_contact=True,
                                                                            one_time_keyboard=True))
    return keyboard


def choose_weight():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='до 10 кг', callback_data='ten'),
        types.InlineKeyboardButton(text='10-25 кг', callback_data='ten_twenty'),
        types.InlineKeyboardButton(text='40 - 70 кг', callback_data='40_70'),
        types.InlineKeyboardButton(text='70 - 100 кг', callback_data='70-100'),
        types.InlineKeyboardButton(text='более 100 кг', callback_data='more100'),
        types.InlineKeyboardButton(text='Не знаю, помогите мне!', callback_data='idk'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


def choose_height():
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.InlineKeyboardButton(text='Менее 3 кв. м.', callback_data='less3'),
        types.InlineKeyboardButton(text='3 - 7 кв. м', callback_data='3-7m'),
        types.InlineKeyboardButton(text='7 - 10 кв. м', callback_data='7-10m'),
        types.InlineKeyboardButton(text='Не знаю, помогите мне!', callback_data='idk'),
        types.InlineKeyboardButton(text='⬅️ Обратно в меню', callback_data='back_to_menu')
    ]
    keyboard.add(*buttons)
    return keyboard


