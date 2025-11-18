from bot.handlers.message_start_handler import MessageStartHandler

from bot.dispatcher import Dispatcher
from tests.mocks import Mock


def test_message_start_handler():
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
            "text": "/start",
        },
    }

    clear_user_data_called = False
    update_user_state_called = False

    def clear_user_history(telegram_id):
        assert telegram_id == 166564
        nonlocal clear_user_data_called
        clear_user_data_called = True

    def update_user_state(telegram_id, state):
        assert telegram_id == 166564
        assert state == "WAIT_FOR_PIZZA_NAME"
        nonlocal update_user_state_called
        update_user_state_called = True

    def get_user(telegram_id: int) -> None:
        assert telegram_id == 166564
        return None

    mock_storage = Mock(
        {
            "clear_user_history": clear_user_history,
            "update_user_state": update_user_state,
            "get_user": get_user,
        }
    )

    send_message_test = []

    def sendMessage(chat_id: int, text: str, **kwargs):
        assert chat_id == 166564
        send_message_test.append({"text": text, "kwargs": kwargs})
        return {"ok": True, "result": {"message_id": 194}}

    mock_messenger = Mock({"sendMessage": sendMessage})
    dispatcher = Dispatcher(mock_storage, mock_messenger)
    message_start_handler = MessageStartHandler()
    dispatcher.add_handlers(message_start_handler)
    dispatcher.dispatch(test_update, dispatcher._storage, dispatcher._messenger)

    assert clear_user_data_called
    assert update_user_state_called
    assert len(send_message_test) == 2
    assert send_message_test[0]["text"] == "🍕 Welcome to Pizza shop!"
    assert send_message_test[1]["text"] == "Please choose pizza type"
