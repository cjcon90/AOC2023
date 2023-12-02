import typing as t
import re
from pathlib import Path

LIMITS = {"red": 12, "green": 13, "blue": 14}


def get_game_id_and_games(line: str) -> t.Tuple[str, str]:
    match = re.match(r"Game (\d+):", line)
    game_id = int(match.group(1))
    games = line.split(":")[1].split(";")
    return game_id, games


def game_is_valid(game) -> bool:
    numcols = game.strip().split(',')
    for numcol in numcols:
        num, col = numcol.split()
        if int(num) > LIMITS[col]:
            return False
    return True


def main() -> None:
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read().strip().splitlines()
    total = 0
    for line in data:
        game_id, games = get_game_id_and_games(line)
        if all(game_is_valid(game) for game in games):
            total += game_id

    print(total)


if __name__ == "__main__":
    main()
