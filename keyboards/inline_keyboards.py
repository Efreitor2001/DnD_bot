from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton


def next_button() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Далее >>>",
        callback_data="next"
    ))
    return builder.as_markup()


def choose_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Подтвердить ✅",
        callback_data="accept"
    ))
    builder.add(InlineKeyboardButton(
        text="<<< Назад",
        callback_data="back"
    ))
    return builder.as_markup()
