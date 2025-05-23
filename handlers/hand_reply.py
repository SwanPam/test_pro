from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import keyboards


other_handler = Router()

@other_handler.message(Command('reply_keyboard'))
async def hi_handler(message: Message):
    keyboard = keyboards.get_reply_keyboard()
    text = f'reply-клавиатура'
    
    await message.answer(text=text, reply_markup=keyboard)

@other_handler.message('hi')
async def hi_handler(message: Message):
    text = f'Сообщение Привет'
    
    await message.reply(text=text)

@other_handler.message(F.text == 'bye')
async def bye_handler(message: Message):
    text = f'Сообщение Пока'
    
    await message.reply(text=text)
