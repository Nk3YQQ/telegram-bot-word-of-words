import requests
from random import shuffle as shuffle_words
from classes.class_basic_word import BasicWord


def load_random_word():
    """
    Функция получает список слов с "jsonkeeper.com",
    выбирает случайное слово, создаёт экземпляр класса
    BasicWord и возвращает данный экземпляр
    """
    response = requests.get('https://www.jsonkeeper.com/b/4DAF')
    words_list = response.json()
    shuffle_words(words_list)
    dict_word = words_list[0]['word']
    dict_subwords = words_list[0]['subwords']
    word = BasicWord(dict_word, dict_subwords)
    return word
