from typing import List, Union

from aiogram.filters import BaseFilter
from aiogram.types import Message


class Admin(BaseFilter):
    def __init__(self, user_ids: Union[int, List[int]]) -> None:
        self.user_ids = user_ids

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.user_ids, int):
            return message.from_user.id == self.user_ids
        return message.from_user.id in self.user_ids
