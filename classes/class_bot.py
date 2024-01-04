from typing import Any

import telebot


class Bot(telebot.TeleBot):
    """
    Класс является абстракцией для создания телеграм-бота
    """

    def __init__(self, api_key: str | None, *args: Any, **kwargs: Any) -> None:
        super().__init__(api_key, *args, **kwargs)
