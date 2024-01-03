import os

from dotenv import load_dotenv

from classes.class_bot import Bot
from classes.class_word_of_words import WordOfWords

load_dotenv()

if __name__ == "__main__":
    bot = Bot(os.getenv("TELEBOT_API"))

    game = WordOfWords(bot)
    game.activate()
    game.run()
