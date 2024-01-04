import pytest

from config import FAKE_JSON_PATH
from saver import JSONSaver
from utils.for_save import get_top_score, open_json_file


@pytest.fixture
def player() -> dict:
    return {"player": "player_name", "score": 8}


def test_saver(player: dict) -> None:
    json_saver = JSONSaver()
    json_saver.save_result(player["player"], player["score"], FAKE_JSON_PATH)

    wrote_data = open_json_file(FAKE_JSON_PATH)
    assert isinstance(wrote_data, list)

    assert (
        json_saver.get_top_result(player["player"], FAKE_JSON_PATH) == f"Максимальное количество угаданных слов: "
        f"{get_top_score(wrote_data, player['player'])}"
    )
