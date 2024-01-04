class Player:
    """
    Класс, содержащий поля: имя пользователя
    и использованные слова пользователя
    """

    user_words: list = []

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def count_user_words(cls) -> int:
        """
        Возвращает количество использованных
        слов пользователем
        """
        return len(Player.user_words)

    @classmethod
    def append_to_user_words(cls, user_word: str) -> None:
        """
        Добавляет использованные слова
        пользователем в user_words
        """
        Player.user_words.append(user_word)

    @classmethod
    def check_user_word(cls, user_word: str) -> bool:
        """
        Проверяет, использовалось ли слово,
        введённое пользользователем до этого
        """
        return user_word in Player.user_words

    def __str__(self) -> str:
        return f"Имя пользователя: {self.name}. Использованные слова пользователя: {', '.join(Player.user_words)}"
