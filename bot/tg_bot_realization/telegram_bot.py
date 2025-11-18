import urllib.request
import json
import os
from bot.domain.messenger import Messenger

from dotenv import load_dotenv

load_dotenv()


class MessengerTelegram(Messenger):

    def makeRequest(self, method: str, **params) -> dict:
        jsonData = json.dumps(params).encode("utf-8")
        print(jsonData)
        request = urllib.request.Request(
            method="POST",
            url=f"{os.getenv('TELEGRAM_BASE_URI')}{os.getenv('TOKEN')}/{method}",
            data=jsonData,
            headers={
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(request) as response:
            responseBody = response.read().decode("utf-8")
            responseJSON = json.loads(responseBody)
            if responseJSON["ok"]:
                return responseJSON["result"]
            else:
                print("not ok")

    def getUpdates(self, **params) -> dict:
        return self.makeRequest("getUpdates", **params)

    def sendMessage(self, chat_id: int, text: str, **params) -> dict:
        return self.makeRequest("sendMessage", chat_id=chat_id, text=text, **params)

    def deleteMessage(self, chat_id: int, message_id: int) -> dict:
        """
        https://core.telegram.org/bots/api#deletemessage
        """
        return self.makeRequest("deleteMessage", chat_id=chat_id, message_id=message_id)

    def answerCallbackQuery(self, callback_query_id: str, **kwargs) -> dict:
        """
        https://core.telegram.org/bots/api#answercallbackquery
        """
        return self.makeRequest(
            "answerCallbackQuery", callback_query_id=callback_query_id, **kwargs
        )
