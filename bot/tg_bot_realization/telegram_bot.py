import logging
import aiohttp
import urllib.request
import json
import os
import time
from bot.domain.messenger import Messenger

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s.%(msecs)03d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class MessengerTelegram(Messenger):
    def __init__(self) -> None:
        self._session: aiohttp.ClientSession | None = None

    async def getSession(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session

    async def makeRequest(self, method: str, **params) -> dict:
        start_time = time.time()
        logger.info(f"[HTTP] → POST {method}")

        try:
            session = await self.getSession()
            async with session.post(
                f"{os.getenv('TELEGRAM_BASE_URI')}{os.getenv('TOKEN')}/{method}",
                json=params,
                headers={"Content-Type": "application/json"},
            ) as response:
                response_json = await response.json()
                print(response_json)
                assert response_json["ok"] == True

                duration_ms = (time.time() - start_time) * 1000
                logger.info(f"[HTTP] ← POST {method} - {duration_ms:.2f}ms")

                return response_json["result"]
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            logger.error(f"[HTTP] ✗ POST {method} - {duration_ms:.2f}ms - Error: {e}")
            raise

    async def getUpdates(self, **params) -> dict:
        return await self.makeRequest("getUpdates", **params)

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()

    async def sendMessage(self, chat_id: int, text: str, **params) -> dict:
        return await self.makeRequest(
            "sendMessage", chat_id=chat_id, text=text, **params
        )

    async def deleteMessage(self, chat_id: int, message_id: int) -> dict:
        """
        https://core.telegram.org/bots/api#deletemessage
        """
        return await self.makeRequest(
            "deleteMessage", chat_id=chat_id, message_id=message_id
        )

    async def answerCallbackQuery(self, callback_query_id: str, **kwargs) -> dict:
        """
        https://core.telegram.org/bots/api#answercallbackquery
        """
        return await self.makeRequest(
            "answerCallbackQuery", callback_query_id=callback_query_id, **kwargs
        )
