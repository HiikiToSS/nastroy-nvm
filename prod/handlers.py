from datetime import *
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import *
from aiogram.fsm.state import State, StatesGroup

import keyboard as keyb


router = Router()
on = 0


class Register(StatesGroup):
    name = State()
    number = State()


@router.message(Command('start'))
async def cmd_start(message:Message):
    await message.answer('Добро пожаловать в Zaebushek')
    await message.answer('В нашем боте вы можете:\n\n'
                         'Начать записывать данные прямо сейчас, тогда напоминание будет приходить каждые 24 часа от момента нажатия на кнопку\n\n'
                         'Указать время, когда Вам будет удобно получать и отвечать на уведомления\n\n'
                         'Вывести статисктику за предыдщие 7 дней\n\n'
                         'Выключить запись и присотановить напоминания')
    await message.answer('Для выбора используйте кнопки ниже:',reply_markup = keyb.instart)


@router.message(Command('stop'))
async def cmd_stop(message:Message):
    global on
    on = 0
    await message.answer('Zaeb остановлен')


@router.message(Command('begin'))
async def cmd_begin(message:Message):
    global on
    on = 1
    dateti = datetime.now()
    delta = timedelta(seconds = 5)
    while on == 1:
        if datetime.now() - dateti >= delta:
            await message.answer('Zaeb')
            dateti = datetime.now()


@router.callback_query(F.data == 'rude')
async def rude(callback: CallbackQuery):
    await callback.answer('Вы наругались на Zaebushek', show_alert=True)
    await callback.message.answer('Сам ПШЛНХЙ')


@router.callback_query(F.data == 'begin')
async def begin(callback: CallbackQuery):
    await callback.answer('Zaeb начался')
    global on
    on = 1
    dateti = datetime.now()
    delta = timedelta(seconds=5)
    while on == 1:
        if datetime.now() - dateti >= delta:
            await callback.message.answer('Zaeb')
            dateti = datetime.now()

@router.callback_query(F.data == 'stop')
async def stop(callback: CallbackQuery):
    global on
    on = 0
    await callback.answer('Скоро закончу')
    await callback.message.answer('Закончил')
