class BasicWord:
    """
    Класс, содержащий поля: исходное слово
    и набор допустимых слов
    """
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_word(self, user_input):
        """
        Возвращает True, если слово есть в списке подслов
        или False, если слова нет в списке
        """
        return user_input in self.subwords

    def count_subwords(self):
        """
        Возвращает количество подслов
        в списке
        """
        return len(self.subwords)

    def __str__(self):
        return f"""Составьте {self.count_subwords()} слов из слова {self.word.upper()}
Слова должны быть не короче {len(min(self.subwords, key=len))} букв"""
