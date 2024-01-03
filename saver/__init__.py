from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from utils.for_save import get_top_five_scores, open_json_file, write_score_to_player, write_to_json_file


class Saver(ABC):
    @abstractmethod
    def save_result(self, player_name: str, score: int, filepath: Path) -> None:
        pass

    @abstractmethod
    def get_top_five_results(self, player_name: str, filepath: Path) -> None:
        pass


class JSONSaver(Saver):
    def save_result(self, player_name: str, score: int, filepath: Path) -> None:
        players_data = open_json_file(filepath)
        upgraded_players_data = write_score_to_player(players_data, player_name, score)
        write_to_json_file(filepath, upgraded_players_data)

    def get_top_five_results(self, player_name: str, filepath: Path) -> Any:
        players_data = open_json_file(filepath)
        return f"Максимальное количество угаданных слов: {get_top_five_scores(players_data, player_name)}"
