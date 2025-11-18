from abc import ABC, abstractmethod


class Messenger(ABC):
    @abstractmethod
    def getUpdates(self, **params) -> dict:
        pass

    @abstractmethod
    def sendMessage(self, chat_id: int, text: str, **params) -> dict:
        pass

    @abstractmethod
    def deleteMessage(self, chat_id: int, message_id: int) -> dict:
        pass

    @abstractmethod
    def answerCallbackQuery(self, callback_query_id: str, **kwargs) -> dict:
        pass
