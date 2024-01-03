import telebot


class Bot(telebot.TeleBot):
    def __init__(self, api_key, *args, **kwargs):
        super().__init__(api_key, *args, **kwargs)
