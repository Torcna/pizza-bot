from bot.dispatcher import Dispatcher
from bot.handlers import get_handlers

from bot.postgres_database.storage_postgres import StoragePostgres
from bot.tg_bot_realization.telegram_bot import MessengerTelegram
from bot.domain.storage import Storage
from bot.domain.messenger import Messenger
from bot.long_polling import start_long_polling


if __name__ == "__main__":
    try:
        storage: Storage = StoragePostgres()
        messenger: Messenger = MessengerTelegram()
        dispatcher = Dispatcher(storage, messenger)
        dispatcher.add_handlers(*get_handlers())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nStop")
