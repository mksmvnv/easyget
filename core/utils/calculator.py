from decimal import Decimal

from utils.currency import get_exchange_rates

from data.config import settings


async def calculator(product: int, logistics: int) -> Decimal:
    rate = await get_exchange_rates()
    amount = (
        (product + settings.logistics.china) * rate + settings.logistics.fee + logistics
    )
    return amount
