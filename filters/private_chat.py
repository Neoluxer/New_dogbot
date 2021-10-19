from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter): # Наследуем от класса BoundFilter

    async def check (self,  message:types.Message):
        return message.chat.type ==types.ChatType.PRIVATE # Летит в хэндлер если выполняется условие