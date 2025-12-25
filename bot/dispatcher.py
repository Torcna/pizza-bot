from bot.handlers.handler import Handler
from bot.domain.storage import Storage
from bot.domain.messenger import Messenger
import logging
import time
import json

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class Dispatcher:
    def __init__(self, storage: Storage, messenger: Messenger) -> None:
        self._handlers: list[Handler] = []
        self._storage: Storage = storage
        self._messenger: Messenger = messenger

    def add_handlers(
        self,
        *handlers: Handler,
    ) -> None:
        for handler in handlers:
            self._handlers.append(handler)

    def _get_telegram_id_from_update(self, update: dict) -> int:
        """Extract telegram_id from update object."""
        if "message" in update:
            return update["message"]["from"]["id"]
        elif "callback_query" in update:
            return update["callback_query"]["from"]["id"]
        return None

    async def dispatch(
        self, update: dict, storage: Storage, messenger: Messenger
    ) -> None:
        # Get user state for handlers that need it
        update_id = update["update_id"]
        start_time = time.time()
        logger.info(f"[DISPATCH {update_id}] → dispatch started 🏃‍♂️")
        try:
            telegram_id = self._get_telegram_id_from_update(update)
            user = await storage.get_user(telegram_id) if telegram_id else None

            user_state = user.get("state") if user else None

            order_json = user["order_json"] if user else "{}"
            if order_json is None:
                order_json = "{}"
            order_json = json.loads(order_json)

            for handler in self._handlers:
                if handler.can_handle(
                    update, user_state, order_json, self._storage, self._messenger
                ):
                    if not await handler.handle(
                        update, user_state, order_json, self._storage, self._messenger
                    ):
                        break

            duration_ms = (time.time() - start_time) * 1000
            logger.info(
                f"[DISPATCH {update_id}] ← dispatch finished - {duration_ms:.2f}ms\n"
            )
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(
                f"[DISPATCH {update_id}] ✗ dispatch failed - {duration_ms:.2f}ms - Error: {e}\n"
            )
            raise
