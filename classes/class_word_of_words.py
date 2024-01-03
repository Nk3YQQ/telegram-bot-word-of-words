from config import JSON_PATH
from classes.class_player import Player
from utils.for_bot import create_panel, create_next_step, check_user_word, info_message, saver, getter
from utils.for_words import load_random_word
from threading import Lock

lock = Lock()


class WordOfWords:
    def __init__(self, bot):
        self.bot = bot

    def activate(self):
        @self.bot.message_handler(commands=['start'])
        def start(message):
            with lock:
                create_panel(message, self.bot, f'Привет, {message.from_user.username}!', 'Меню')
                create_next_step(self.bot, message, menu)

        @self.bot.message_handler(commands=['menu'])
        def menu(message):
            with lock:
                if message.text == 'Меню':
                    create_panel(message, self.bot, f'Выберите один из разделов:', 'Начать игру', 'Максимальный результат',
                                 'Помощь')
                    create_next_step(self.bot, message, on_click)
                else:
                    self.bot.send_message(message.chat.id, 'Я Вас не понял :(')
                    create_next_step(self.bot, message, menu)

        @self.bot.message_handler()
        def on_click(message):
            with lock:
                if message.text == 'Начать игру':
                    create_panel(message, self.bot, 'Отлично! Если вы готовы, нажмите "Готов".', 'Готов',
                                 'Вернуться в меню')
                    create_next_step(self.bot, message, game)

                elif message.text == 'Максимальный результат':
                    player = Player(message.from_user.username)
                    self.bot.send_message(message.chat.id, getter(player.name, JSON_PATH))
                    create_next_step(self.bot, message, on_click)

                elif message.text == 'Помощь':
                    self.bot.send_message(message.chat.id, info_message())
                    create_next_step(self.bot, message, on_click)

                else:
                    self.bot.send_message(message.chat.id, 'Я Вас не понял :(')
                    create_next_step(self.bot, message, on_click)

        @self.bot.message_handler()
        def game(message):
            with lock:
                if message.text == 'Готов':
                    create_panel(message, self.bot, 'Игра начинается!', 'Стоп')
                    player = Player(message.from_user.username)
                    word_info = load_random_word()
                    self.bot.send_message(message.chat.id, word_info)
                    process_word(message, player, word_info)

                elif message.text == 'Вернуться в меню':
                    create_panel(message, self.bot, 'Возвращаю Вас в меню.', 'Начать игру',
                                 'Максимальный результат', 'Помощь')
                    create_next_step(self.bot, message, on_click)

                else:
                    self.bot.send_message(message.chat.id, 'Я Вас не понял :(')
                    create_next_step(self.bot, message, game)

        def process_word(message, player, word_info):
            if len(player.user_words) == len(word_info.subwords):
                self.bot.send_message(message.chat.id, f'Вы угадали все слова. Игра завершена!')
                saver(player.name, len(player.user_words), JSON_PATH)
                return

            self.bot.send_message(message.chat.id, f"Введите слово:")
            create_next_step(self.bot, message, lambda m: handle_user_input(m, player, word_info))

        def handle_user_input(message, player, word_info):
            user_word = message.text.lower()

            check_user_word(user_word, player, self.bot, message, process_word, word_info, menu)

    def run(self):
        self.bot.polling(none_stop=True)
