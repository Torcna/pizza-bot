import bot.databaseClient

from bot.handlers.handler import Handler


class DatabaseLogger(Handler):

    def can_handle(self, update: dict, state: str, order_jsonn: dict) -> bool:
        return True

    def handle(self, update: dict, state: str, order_jsonn: dict) -> bool:
        bot.databaseClient.persistUpdate(update)
        return True
