import time
from bot.dispatcher import Dispatcher


def start_long_polling(dispatcher: Dispatcher) -> None:
    offsetCounter = 0
    while True:
        updates = dispatcher._messenger.getUpdates(offset=offsetCounter)
        for upd in updates:
            dispatcher.dispatch(upd, dispatcher._storage, dispatcher._messenger)
            offsetCounter = max(offsetCounter, upd["update_id"] + 1)
            print(".", end="", flush=True)
        time.sleep(1)
