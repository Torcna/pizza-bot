from bot.dispatcher import Dispatcher
from bot.handlers import get_handlers
from bot.sqlite_database.storage_sqlite import StorageSqlite
from bot.tg_bot_realization.telegram_bot import MessengerTelegram
from bot.domain.storage import Storage
from bot.domain.messenger import Messenger
from bot.long_polling import start_long_polling


if __name__ == "__main__":
    try:
        storage: Storage = StorageSqlite()
        messenger: Messenger = MessengerTelegram()
        dispatcher = Dispatcher(storage, messenger)
        dispatcher.add_handlers(*get_handlers())
        start_long_polling(dispatcher)
    except KeyboardInterrupt:
        print("\nStop")
