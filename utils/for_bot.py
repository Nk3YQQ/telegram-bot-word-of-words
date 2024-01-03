from pathlib import Path
from typing import Any

from telebot import types

from classes.class_basic_word import BasicWord
from classes.class_bot import Bot
from classes.class_player import Player
from config import JSON_PATH
from saver import JSONSaver


def create_panel(message: Any, bot: Bot, bot_message: str, *bottom_names: Any) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for bottom_name in bottom_names:
        bottom = types.KeyboardButton(bottom_name)
        markup.row(bottom)

    bot.send_message(message.chat.id, bot_message, reply_markup=markup)


def create_next_step(bot: Bot, message: Any, next_handler: Any) -> None:
    bot.register_next_step_handler(message, next_handler)


def check_user_word(
    user_word: str, player: Player, bot: Bot, message: Any, process_word: Any, word_info: BasicWord, menu: Any
) -> None:
    if user_word == "стоп":
        create_panel(message, bot, f"Игра заверена. Количество угаданных слов - {len(player.user_words)}.", "Меню")
        saver(player.name, len(player.user_words), JSON_PATH)
        create_next_step(bot, message, menu)
        return

    if player.check_user_word(user_word):
        bot.send_message(message.chat.id, "Это слово уже использовано. Попробуйте другое.")
        process_word(message, player, word_info)
    elif len(user_word) < len(min(word_info.subwords, key=len)):
        bot.send_message(message.chat.id, "Слишком короткое слово. Попробуйте другое.")
        process_word(message, player, word_info)
    elif word_info.check_word(user_word):
        player.append_to_user_words(user_word)
        bot.send_message(message.chat.id, f"Верно! Количество угаданных слов - {player.count_user_words()}.")
        process_word(message, player, word_info)
    else:
        bot.send_message(message.chat.id, "Неверно. Попробуйте другое слово.")
        process_word(message, player, word_info)


def info_message() -> str:
    return (
        'Для того, чтобы начать игру, нужно нажать на кнопку "Начать игру". Правила игры простые - Вам нужно '
        "будет угадать как можно больше слов. Если Вам надоест угадывать слова, то Вы можете начать на кнопку "
        '"Стоп", и Ваш результат сохранится. Для того, чтобы посмотреть Ваш максимальный результат, нажмите на '
        'кнопку "Максимальный результат".'
    )


def saver(player_name: str, word_count: int, filepath: Path) -> None:
    json_saver = JSONSaver()
    json_saver.save_result(player_name, word_count, filepath)


def getter(player_name: str, filepath: Path) -> Any:
    json_saver = JSONSaver()
    return json_saver.get_top_five_results(player_name, filepath)
