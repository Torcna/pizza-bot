from bot.handlers.database_logger import DatabaseLogger
from bot.handlers.ensure_user_exists import EnsureUserExists
from bot.handlers.message_start_handler import MessageStartHandler
from bot.handlers.pizza_selection_handler import PizzaSelectionHandler
from bot.handlers.pizza_size_handler import PizzaSizeHandler
from bot.handlers.drinks_handler import DrinksHandler
from bot.handlers.order_finishing_handler import OrderFinishingHandler


def get_handlers() -> list:
    return [
        DatabaseLogger(),
        EnsureUserExists(),
        MessageStartHandler(),
        PizzaSelectionHandler(),
        PizzaSizeHandler(),
        DrinksHandler(),
        OrderFinishingHandler(),
    ]
