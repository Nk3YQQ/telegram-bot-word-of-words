import json
from pathlib import Path
from typing import Any


def open_json_file(filepath: Path) -> list[dict] | Any:
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def write_to_json_file(filepath: Path, data: Any) -> Any:
    with open(filepath, "w", encoding="utf-8") as file:
        return json.dump(data, file, ensure_ascii=False, indent=4)


def write_score_to_player(players_data: Any, player_name: str, score: int) -> Any:
    player_exists = False
    for player_data in players_data:
        if player_data.get("name") == player_name:
            player_data["score"].append(score)
            player_exists = True
    if not player_exists:
        new_player = {"name": player_name, "score": [score]}
        players_data.append(new_player)
    return players_data


def get_top_five_scores(players_data: Any, player_name: str) -> Any:
    for player_data in players_data:
        if player_data.get("name") == player_name:
            return max(player_data["score"])
