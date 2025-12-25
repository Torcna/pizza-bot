from bot.handlers.handler import Handler
from bot.domain.storage import Storage
from bot.domain.messenger import Messenger


class EnsureUserExists(Handler):
    def can_handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool:
        # This handler should run for any update that has a user ID
        return "message" in update and "from" in update["message"]

    async def handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool:
        telegram_id = update["message"]["from"]["id"]

        await storage.ensure_user_exists(telegram_id)

        # Continue processing with other handlers
        return True
