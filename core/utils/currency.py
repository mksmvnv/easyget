import aiohttp

from decimal import Decimal

from data.config import settings


async def get_exchange_rates() -> Decimal:
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.links.api) as response:
            if response.status != 200:
                raise ValueError(f"API request failed with status {response.status}")

            data = await response.json()
            rub = data["data"]["RUB"]["value"]
            cny = data["data"]["CNY"]["value"]

            return (Decimal(rub) / Decimal(cny)).quantize(Decimal("0.01")) + 1
