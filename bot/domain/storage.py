from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def recreate_db() -> None:
        pass

    @abstractmethod
    def persistUpdate(update: dict) -> None:
        pass

    @abstractmethod
    def ensure_user_exists(telegram_id: int) -> None:
        pass

    @abstractmethod
    def get_user(telegram_id: int) -> dict:
        pass

    @abstractmethod
    def update_user_state(telegram_id: int, state: str) -> None:
        pass

    @abstractmethod
    def update_user_data(telegram_id: int, data: dict) -> None:
        pass

    @abstractmethod
    def clear_user_history(telegram_id: int) -> None:
        pass
