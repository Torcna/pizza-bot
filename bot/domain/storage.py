from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    async def recreate_db() -> None:
        pass

    @abstractmethod
    async def persistUpdate(update: dict) -> None:
        pass

    @abstractmethod
    async def ensure_user_exists(telegram_id: int) -> None:
        pass

    @abstractmethod
    async def get_user(telegram_id: int) -> dict:
        pass

    @abstractmethod
    async def update_user_state(telegram_id: int, state: str) -> None:
        pass

    @abstractmethod
    async def update_user_order(telegram_id: int, data: dict) -> None:
        pass

    @abstractmethod
    async def clear_user_history(telegram_id: int) -> None:
        pass
