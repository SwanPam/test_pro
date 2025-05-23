from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_test_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Кнопка 1', callback_data=f'button_1')],
                                                 [InlineKeyboardButton(text='Кнопка 2', callback_data=f'button_2')],
                                                 [InlineKeyboardButton(text='Главное меню', callback_data=f'main_menu')]])
    
