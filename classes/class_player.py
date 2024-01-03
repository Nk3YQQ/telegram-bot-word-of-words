class Player:
    user_words = []
    """
    Класс, содержащий поля: имя пользователя
    и использованные слова пользователя
    """
    def __init__(self, name):
        self.name = name

    @classmethod
    def count_user_words(cls):
        """
        Возвращает количество использованных
        слов пользователем
        """
        return len(Player.user_words)

    @classmethod
    def append_to_user_words(cls, user_word):
        """
        Добавляет использованные слова
        пользователем в user_words
        """
        Player.user_words.append(user_word)

    @classmethod
    def check_user_word(cls, user_word):
        """
        Проверяет, использовалось ли слово,
        введённое пользользователем до этого
        """
        return user_word in Player.user_words

    def __str__(self):
        return f"""Имя пользователя: {self.name}
Использованные слова пользователя: {', '.join(Player.user_words)}"""