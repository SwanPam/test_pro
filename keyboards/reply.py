from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# Ещё бы вспомнить, откуда их импортировать, XD, мало с ними работал

def get_reply_keyboard() -> ReplyKeyboardMarkup: # Стрелка просто указывает, какой тип возвращает функция, будет видно, когда будешь использовать
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='hi')],
                                         [KeyboardButton(text='bye')]])