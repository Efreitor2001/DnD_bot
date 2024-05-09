import asyncio
import logging

from create_bot import dp, bot
from handlers import bot_commands


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(bot_commands.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
