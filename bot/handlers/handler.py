from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def can_handle(self, update: dict, state: str, order_json: dict) -> bool: ...

    @abstractmethod
    def handle(self, update: dict, state: str, order_json: dict) -> bool:
        """
        returns True if this handler is NOT the last one
        returns False if further processing is restricted
        """

        pass
