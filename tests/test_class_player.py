import pytest

from classes.class_player import Player


@pytest.fixture
def word_info() -> dict:
    return {"word": "питон", "subwords": ["пони", "тон", "ион", "опт", "пот", "тип", "топ", "пион", "понт"]}


def test_class_player(word_info: dict) -> None:
    subwords = word_info["subwords"]
    player = Player("player_name")

    player.append_to_user_words(subwords[0])
    player.append_to_user_words(subwords[1])
    player.append_to_user_words(subwords[2])

    assert player.count_user_words() == 3

    assert player.check_user_word(subwords[0]) is True
    assert player.check_user_word(subwords[3]) is False

    assert str(player) == "Имя пользователя: player_name. Использованные слова пользователя: пони, тон, ион"
