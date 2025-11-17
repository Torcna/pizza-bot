import urllib.request
import json
import os

from dotenv import load_dotenv

load_dotenv()


def makeRequest(method: str, **params) -> dict:
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


def getUpdates(**params) -> dict:
    return makeRequest("getUpdates", **params)


def sendMessage(chat_id: int, text: str, **params) -> dict:
    return makeRequest("sendMessage", chat_id=chat_id, text=text, **params)


def getMe() -> dict:
    return makeRequest("getMe")


def sendPhoto(chat_id: int, photo: str, **params) -> dict:
    return makeRequest("sendPhoto", chat_id=chat_id, photo=photo, **params)


def deleteMessage(chat_id: int, message_id: int) -> dict:
    """
    https://core.telegram.org/bots/api#deletemessage
    """
    return makeRequest("deleteMessage", chat_id=chat_id, message_id=message_id)


def answerCallbackQuery(callback_query_id: str, **kwargs) -> dict:
    """
    https://core.telegram.org/bots/api#answercallbackquery
    """
    return makeRequest(
        "answerCallbackQuery", callback_query_id=callback_query_id, **kwargs
    )
