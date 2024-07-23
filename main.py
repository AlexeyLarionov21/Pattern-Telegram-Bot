import asyncio
from aiogram import Bot, Dispatcher
from handlers.handlers import router
from config import TOKEN_TELEGRAM_BOT

async def main():
    bot = Bot(token=TOKEN_TELEGRAM_BOT)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Bot enabled')
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot disabled")