from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import keyboards
# Используем start_router
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()')

@start_router.message(Command('start_2'))
async def cmd_start_2(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')

@start_router.message(F.text == '/start_3')
async def cmd_start_3(message: Message):
    await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')

# Для message используется message: Message
@start_router.message(F.text == 'keyboard')
async def get_keyboard_handler(message: Message):
    keyboard = keyboards.get_test_keyboard()
    text = f'Привет. Я клавиатура.'
    await message.answer(text=text, reply_markup=keyboard)

# Для callback_query в функции используется callback: CallbackQuery
@start_router.callback_query(F.data.startswith('button_'))
async def button_all_hand(callback: CallbackQuery):
    user_id, message = callback.from_user.id, callback.data
    
    if message == 'button_1':
        text = f'Привет от кнопки {message}. Личный обработчик. Твой id: {user_id}'
        await callback.message.answer(text=text)
        
    text = f'Привет от кнопки {message}. Общий обработчик.'
    await callback.message.answer(text=text)
    await callback.answer('') # Это далается, чтобы кнопка после нажатия не продолжала мигать

@start_router.callback_query(F.data == f'main_menu')
@start_router.message(Command('Меню')) # Красивее всего, чем F.data == '/Меню' для комманды
async def main_menu_handler(update: Message | CallbackQuery):
    text = f'Добро пожаловть на главное меню!'
    # Смотри, в зависимости от того, что мы приняли - сообщение или callback - мы должны по разному отправить ответ
    # Если применить только update.answer() к обоим, мы на callback-е словим ошибку, ибо он не так обрабатывается
    # callback - await update.message.answer(text=text)
    # message  - await update.answer(text=text)
    if isinstance(update, Message): # Является ли update экземпляром класса Message
        await update.answer(text=(text + "от комманды")) # На будущее, лучше не использовать позиционное присвоение, а так, как тут
    elif isinstance(update, CallbackQuery):
        await update.message.answer(text=(text + "от кнопки"))
        await update.answer('') # Это далается, чтобы кнопка после нажатия не продолжала мигать

# Основные - это два: message, callback, есть дополнительные, об этом лучше отдельно почитать
# callback: CallbackQuery - это значит, что аргумент callback типа CallbakQuery
# Но это условное, для того, что интерпретатор подсказывал и пользователи понимали, с каким объектом работаю
# @start_router.callback_query(F.data == 'button_1') - это, после собачки, называется декоратором
