from aiogram import Router
from .handler import start_router
from .hand_reply import other_handler

all_handlers = Router()
all_handlers.include_router(start_router)
all_handlers.include_router(other_handler)

# Здесь получаешь доступ к тому, что импортируешь, в нашем случаи, даже так ко всему
# Хороший-правильный способ инсклюдить рутеры
# Когда будет много обработчиков - их вообще желательно разбивать по файлам, а-ля обработчик пользовательские, оплаты и т.д.
# Тогда будет через __init__.py удобно их инклюдить
# В ином случаи каждый обработчик пришлось бы инклюдить в _main_.py
