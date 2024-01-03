import os

from classes.class_word_of_words import WordOfWords

from dotenv import load_dotenv

from classes.class_bot import Bot

load_dotenv()

if __name__ == '__main__':
    bot = Bot(os.getenv("TELEBOT_API"))

    game = WordOfWords(bot)
    game.activate()
    game.run()
