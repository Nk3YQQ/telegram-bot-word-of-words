from utils.for_save import open_json_file, write_to_json_file, write_score_to_player, get_top_five_scores
from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def save_result(self, player_name, score, filepath):
        pass

    @abstractmethod
    def get_top_five_results(self, player_name, filepath):
        pass


class JSONSaver(Saver):
    def save_result(self, player_name, score, filepath):
        players_data = open_json_file(filepath)
        upgraded_players_data = write_score_to_player(players_data, player_name, score)
        write_to_json_file(filepath, upgraded_players_data)

    def get_top_five_results(self, player_name, filepath):
        players_data = open_json_file(filepath)
        return f'Максимальное количество угаданных слов: {get_top_five_scores(players_data, player_name)}'
