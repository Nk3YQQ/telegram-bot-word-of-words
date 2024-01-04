from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from utils.for_save import get_top_score, open_json_file, write_score_to_player, write_to_json_file


class Saver(ABC):
    """
    Класс является абстракцией для сохранения результата пользователя
    """

    @abstractmethod
    def save_result(self, player_name: str, score: int, filepath: Path) -> None:
        """
        Абстрактный метод реализует сохранение результатов пользователя
        """
        pass

    @abstractmethod
    def get_top_result(self, player_name: str, filepath: Path) -> None:
        """
        Абстрактный метод выводит лучшей результат пользователя
        """
        pass


class JSONSaver(Saver):
    """
    Класс работает с сохранением результата пользователя в json-файл
    """

    def save_result(self, player_name: str, score: int, filepath: Path) -> None:
        """
        Метод реализует сохранение результатов пользователя в json-файл
        """
        players_data = open_json_file(filepath)
        upgraded_players_data = write_score_to_player(players_data, player_name, score)
        write_to_json_file(filepath, upgraded_players_data)

    def get_top_result(self, player_name: str, filepath: Path) -> Any:
        """
        Метод выводит лучшей результат пользователя из json-файла
        """
        players_data = open_json_file(filepath)
        return f"Максимальное количество угаданных слов: {get_top_score(players_data, player_name)}"
