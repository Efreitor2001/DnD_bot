from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

import fsm

router = Router()


@router.message(StateFilter(None), Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer_photo(photo='https://imgur.com/a/l0bT5g2',
                               caption=
                                        "Вы входите в здание гильдии авантюристов и подходите к стойке регистрации.\n\n"
                                        "К Вам подходит пышногрудая эльфийка и мило улыбается.\n\n"
                                        "«Приветствую, авантюрист! Ты видимо тут впервые? Пожалуйста, заполни эту анкету».\n\n"
                                        "Она протягивает вам лист с анкетой.\n\n"
                                        "Вы берёте перо и анкету, идёте к ближайшему свободному столику, садитесь и внимательно изучаете лист.")

    await message.answer_photo(photo='https://imgur.com/a/jwN6ZPh',
                               caption=
                                        "Внимательно изучив анкету, Вы вписываете своё имя. \n\n"
                                        "(Введите имя персонажа:)")

    await state.set_state(fsm.Character.character_name)


@router.message(fsm.Character.character_name, F.text)
async def character_age(message: Message, state: FSMContext):
    await state.update_data(character_name=message.text)
    await message.answer("Тебя зовут " + message.text)
    await state.set_state(fsm.Character.character_age)
    await message.answer("Далее Вы указали Ваш возраст...\n"
                         "(Введите возраст персонажа:) ")

    await state.set_state(fsm.Character.character_age)


@router.message(fsm.Character.character_age, F.text)
async def character_height(message: Message, state: FSMContext):
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
async def character_weight(message: Message, state: FSMContext):
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
async def character_eyes(message: Message, state: FSMContext):
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
async def character_hair(message: Message, state: FSMContext):
    await state.update_data(character_eyes=message.text)
    await message.answer("Твои глаза " + message.text)
    await message.answer("Теперь Вы описали Ваши волосы\n(Опишите волосы персонажа:)")
    await state.set_state(fsm.Character.character_race)


@router.message(fsm.Character.character_race, F.text)
async def character_race(message: Message, state: FSMContext):
    await state.update_data(character_hair=message.text)
    await message.answer("Твои волосы " + message.text)
    await message.answer("Теперь Вы указали Вашу расу\n(Выберите расу персонажа:)")
    await state.set_state(None)

