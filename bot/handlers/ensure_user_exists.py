from bot.databaseClient import ensure_user_exists
from bot.handlers.handler import Handler


class EnsureUserExists(Handler):
    def can_handle(self, update: dict, state: str, data: dict) -> bool:
        # This handler should run for any update that has a user ID
        return "message" in update and "from" in update["message"]

    def handle(self, update: dict, state: str, data: dict) -> bool:
        telegram_id = update["message"]["from"]["id"]

        ensure_user_exists(telegram_id)

        # Continue processing with other handlers
        return True
