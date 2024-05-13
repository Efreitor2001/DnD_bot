from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

import fsm
from keyboards.change_race_keyboard import race_kb
from keyboards.inline_keyboards import next_button

router = Router()
available_race_names = ["Ааракокра",]


@router.message(Command("start"))
async def start(message: Message):
    await message.answer_photo(photo='https://imgur.com/a/l0bT5g2',
                               caption=
                                        "Вы входите в здание гильдии авантюристов и подходите к стойке регистрации.\n\n"
                                        "К Вам подходит пышногрудая эльфийка и мило улыбается.\n\n"
                                        "«Приветствую, авантюрист! Ты видимо тут впервые? Пожалуйста, заполни эту анкету».\n\n"
                                        "Она протягивает вам лист с анкетой.\n\n"
                                        "Вы берёте перо и анкету, идёте к ближайшему свободному столику, садитесь и внимательно изучаете лист.",
                               reply_markup=next_button())


@router.callback_query(StateFilter(None), F.data == "next")
async def character_list(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_caption(caption=callback.message.caption, reply_markup=None)
    await callback.message.answer_photo(photo='https://imgur.com/a/jwN6ZPh',
                               caption=
                               "Внимательно изучив анкету, Вы вписываете своё имя. \n\n"
                               "(Введите имя персонажа:)")
    await callback.answer()
    await state.set_state(fsm.Character.character_name)


@router.message(fsm.Character.character_name, F.text)
async def character_name(message: Message, state: FSMContext):
    await state.update_data(character_name=message.text)
    await message.answer("Тебя зовут " + message.text)
    await state.set_state(fsm.Character.character_age)
    await message.answer("Далее Вы указали Ваш возраст...\n"
                         "(Введите возраст персонажа:) ")

    await state.set_state(fsm.Character.character_age)


@router.message(fsm.Character.character_age, F.text)
async def character_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(character_age=message.text)
        await message.answer("Твой возраст " + message.text)
        await message.answer("Теперь Вы указали Ваш рост\n(Введите рост персонажа в сантиметрах:)")
        await state.set_state(fsm.Character.character_height)
    else:
        await message.answer("Вы поняли, что написали какой-то бред, стёрли написанное и попытались ещё раз\n"
                             "(Введите возраст персонажа цифрами:)")
        await state.set_state(fsm.Character.character_age)


@router.message(fsm.Character.character_height, F.text)
async def character_height(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(character_height=message.text)
        await message.answer("Твой рост " + message.text + " см.")
        await message.answer("Теперь Вы указали Ваш вес\n(Введите вес персонажа в килограммах:)")
        await state.set_state(fsm.Character.character_weight)
    else:
        await message.answer("Вы поняли, что написали какой-то бред, стёрли написанное и попытались ещё раз\n"
                             "(Введите рост персонажа цифрами:)")
        await state.set_state(fsm.Character.character_height)


@router.message(fsm.Character.character_weight, F.text)
async def character_weight(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(character_weight=message.text)
        await message.answer("Твой вес " + message.text + " кг.")
        await message.answer("Теперь Вы описали Ваши глаза\n(Опишите глаза персонажа:)")
        await state.set_state(fsm.Character.character_eyes)
    else:
        await message.answer("Вы поняли, что написали какой-то бред, стёрли написанное и попытались ещё раз\n"
                             "(Введите Вес персонажа цифрами:)")
        await state.set_state(fsm.Character.character_weight)


@router.message(fsm.Character.character_eyes, F.text)
async def character_eyes(message: Message, state: FSMContext):
    await state.update_data(character_eyes=message.text)
    await message.answer("Твои глаза " + message.text)
    await message.answer("Теперь Вы описали Ваши волосы\n(Опишите волосы персонажа:)")
    await state.set_state(fsm.Character.character_hair)


@router.message(fsm.Character.character_hair, F.text)
async def character_hair(message: Message, state: FSMContext):
    await state.update_data(character_hair=message.text)
    await message.answer("Твои волосы " + message.text)
    await message.answer("Теперь Вы указали Вашу расу\n(Выберите расу персонажа:)", reply_markup=race_kb())
    await state.set_state(fsm.Character.character_race)


@router.message(fsm.Character.character_race, F.text.in_(available_race_names))
async def character_race(message: Message, state: FSMContext):
    if message.text == "Ааракокра":
        await message.answer(text="[Описание расы](https://dnd.su/race/92-aarakocra/#osobennosti_aarakokr)\n\n"
                                  "*ОСОБЕННОСТИ ААРАКОКР*\n\n"
                                  "У вас, как у ааракокры, есть некоторые общие особенности с вашим народом\. "
                                  "Начиная с 1 уровня вы можете летать на высокой скорости, что исключительно эффективно"
                                  " при одних обстоятельствах и чрезвычайно опасно при других\. "
                                  "__Игра за ааракокру требует специального разрешения от Мастера\.__\n\n"
                                  "_*Увеличение характеристик\.*_ Значение вашей *Ловкости увеличивается на 2*, а значение *Мудрости увеличивается на 1\.*\n\n"
                                  "_*Возраст\.*_ Ааракокры достигают зрелости к 3 годам\. Обычно ааракокры не живут дольше 30 лет\.\n\n"
                                  "_*Мировоззрение\.*_ Любое\.\n\n"
                                  "_*Размер\.*_ Рост ааракокр около 5 футов \(1,5 метра\)\. Их тела стройные и лёгкие, а вес "
                                  "может быть в диапазоне от 80 до 100 фунтов \(от 36 до 45 килограмм\)\. *Ваш размер — Средний*\.\n\n"
                                  "_*Скорость*_\. Ваша базовая скорость ходьбы составляет *25 футов*\.\n\n"
                                  "_*Полёт\.*_ Вы можете летать со скоростью 50 футов\. Для этого вы __*не должны носить ни средний, ни тяжёлый доспех*__\.\n\n"
                                  "_*Когти\.*_ Вы владеете своей безоружной атакой, которая причиняет при попадании *рубящий урон 1к4*\.\n\n"
                                  "_*Язык\.*_ Вы разговариваете, читаете и пишете на *Общем, Ауране и языке Ааракокр*\.\n\n"
                                  "_*Предыстория\.*_ Предыстории, которые наиболее подходят ааракокрам, это *Мудрец, Отшельник или Чужеземец*\.", parse_mode=ParseMode.MARKDOWN_V2)
