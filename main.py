import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import client, admin, payments, posts, schedule, settings
from database.db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def main():
    # Инициализация БД
    await init_db()
    
    # Подключаем роутеры
    dp.include_router(settings.router)
    dp.include_router(client.router)
    dp.include_router(admin.router)
    dp.include_router(payments.router)
    dp.include_router(posts.router)
    dp.include_router(schedule.router)
    
    logger.info("Бот запущен!")
    
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
