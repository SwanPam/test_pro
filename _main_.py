import asyncio
import logging
# Используем all_handlers
from handlers import all_handlers
from core import dp, bot



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def main():
    # Используем все
    dp.include_router(all_handlers)
    # Если не было объединённого, пришлось бы так инклюдить каждый
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(f'Бот закончил работу прерыванием пользователя!')