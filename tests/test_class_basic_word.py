import pytest

from classes.class_basic_word import BasicWord


@pytest.fixture
def word_info() -> dict:
    return {"word": "питон", "subwords": ["пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"]}


def test_class_basic_word(word_info: dict) -> None:
    word = word_info["word"]
    subwords = word_info["subwords"]

    basic_word = BasicWord(word, subwords)

    assert basic_word.check_word("пони") is True
    assert basic_word.check_word("бар") is False

    assert basic_word.count_subwords() == 9

    assert str(basic_word) == "Составьте 9 слов из слова ПИТОН. " "Слова должны быть не короче 3 букв"
