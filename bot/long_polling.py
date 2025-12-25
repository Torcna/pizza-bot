import time
from bot.dispatcher import Dispatcher


async def start_long_polling(dispatcher: Dispatcher) -> None:
    offsetCounter = 0
    while True:
        updates = await dispatcher._messenger.getUpdates(offset=offsetCounter)
        for upd in updates:
            offsetCounter = max(offsetCounter, upd["update_id"] + 1)
            await dispatcher.dispatch(upd, dispatcher._storage, dispatcher._messenger)

            print(".", end="", flush=True)
        time.sleep(1)
