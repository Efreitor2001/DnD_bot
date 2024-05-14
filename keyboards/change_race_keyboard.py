from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def race_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Ааракокра")
    kb.button(text="Test1")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите расу персонажа", one_time_keyboard=True)
