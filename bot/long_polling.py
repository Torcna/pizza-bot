import time
import bot.tgClient
from bot.dispatcher import Dispatcher


def start_long_polling(dispatcher: Dispatcher) -> None:
    offsetCounter = 0
    while True:
        updates = bot.tgClient.getUpdates(offset=offsetCounter)
        for upd in updates:
            dispatcher.dispatch(upd)
            offsetCounter = max(offsetCounter, upd["update_id"] + 1)
            print(".", end="", flush=True)
        time.sleep(1)
