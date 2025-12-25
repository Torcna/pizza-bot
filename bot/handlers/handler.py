from abc import ABC, abstractmethod
from bot.domain.storage import Storage
from bot.domain.messenger import Messenger


class Handler(ABC):
    @abstractmethod
    def can_handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool: ...

    @abstractmethod
    async def handle(
        self,
        update: dict,
        state: str,
        order_json: dict,
        storage: Storage,
        messenger: Messenger,
    ) -> bool:
        """
        returns True if this handler is NOT the last one
        returns False if further processing is restricted
        """

        pass
