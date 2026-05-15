import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers.start import register_start_handlers
from handlers.facts import register_facts_handlers
from handlers.detective import register_detective_handlers

dp = Dispatcher()

register_start_handlers(dp)
register_facts_handlers(dp)
register_detective_handlers(dp)

async def main():
    bot = Bot(token=TOKEN)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка: {e}")
        

if __name__ == "__main__":
    asyncio.run(main())