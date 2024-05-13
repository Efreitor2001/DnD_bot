from aiogram.filters.state import StatesGroup, State


class Character(StatesGroup):
    character_name = State()
    character_age = State()
    character_height = State()
    character_eyes = State()
    character_weight = State()
    character_hair = State()
    character_class = State()
    character_race = State()
