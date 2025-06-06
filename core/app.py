import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from handlers import basic, callback

from data.config import settings


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - "
        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
        datefmt="%d-%m-%Y %I:%M:%S",
    )

    bot = Bot(
        token=settings.personal.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    dp.include_routers(basic.router, callback.router)

    await dp.start_polling(bot, timeout=10)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Kill")
