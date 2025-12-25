from bot.handlers.handler import Handler
from bot.domain.storage import Storage
from bot.domain.messenger import Messenger


class DatabaseLogger(Handler):

    def can_handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool:
        return True

    async def handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool:
        await storage.persistUpdate(update)
        return True
