from bot.handlers.database_logger import DatabaseLogger

from bot.dispatcher import Dispatcher
from tests.mocks import Mock


def test_update_database_logger():
    test_update = {
        "update_id": 639561807,
        "message": {
            "message_id": 194,
            "from": {
                "id": 166564,
                "is_bot": False,
                "first_name": "TEST_USER1",
                "last_name": "TEST_USER2",
                "username": "TEST_USER12",
                "language_code": "ru",
                "is_premium": True,
            },
            "chat": {
                "id": 166564,
                "first_name": "TEST_USER1",
                "last_name": "TEST_USER2",
                "username": "TEST_USER12",
                "type": "private",
            },
            "date": 1763459583,
            "text": "MESSAGE TEXT",
        },
    }

    persist_update_called = False

    def persistUpdate(payload):
        nonlocal persist_update_called
        persist_update_called = True
        assert payload == test_update

    def get_user(telegram_id: int) -> None:
        assert telegram_id == 166564
        return None

    mock_storage = Mock(
        {
            "persistUpdate": persistUpdate,
            "get_user": get_user,
        }
    )
    mock_messenger = Mock({})

    dispatcher = Dispatcher(mock_storage, mock_messenger)
    update_logger = DatabaseLogger()
    dispatcher.add_handlers(update_logger)
    dispatcher.dispatch(test_update, dispatcher._storage, dispatcher._messenger)
    assert persist_update_called
