from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

# @dp.message_handler(text='/invoice')
from states import Test


@dp.message_handler(Command('invoice'))
async def enter_test(message: types.Message):
    await message.answer("Вы начали формирование Счета.\n"
                         "Введите Покупателя:")


    await Test.first()
@dp.message_handler(state=Test.Q1)
async def answer_q1(message:types.Message,state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data["answer1"] = answer


    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q1(message:types.Message,state: FSMContext):
    data = await state.get_data() #Достаем данные из машины состояний - словарь
    answer1 = data.get("answer1")
    answer2 = message.text
    await message.answer(f'Ответ 1: {answer1}\n'
                         f'Ответ 2: {answer2}')

    async with state.proxy() as data:
        data["answer2"] = answer2

    await state.finish() # Сбрасывается состояние и сбрасываются данные
    await state.reset_state(with_data=False) # Сбрасывает состояние но не данные