import telebot

from classes.class_bot import Bot
from classes.class_word_of_words import WordOfWords


def test_class_class_word_of_words() -> None:
    bot = Bot("your_api_key")
    assert isinstance(bot, telebot.TeleBot)

    game = WordOfWords(bot)
    assert game.activate() is None
