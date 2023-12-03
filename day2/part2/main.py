import typing as t
from pathlib import Path

LIMITS = {"red": 12, "green": 13, "blue": 14}


def get_maxs(games) -> t.Dict[str, int]:
    numvals = {}
    for game in games:
        numcols = game.strip().split(',')
        for numcol in numcols:
            num, col = numcol.strip().split()
            numvals.setdefault(col, [])
            numvals[col].append(int(num))

    return {col: max(numvals[col]) for col in numvals.keys()}


def main(data) -> None:
    total = 0
    for line in data:
        games = line.split(":")[1].split(";")
        maxs = get_maxs(games)
        power = 1
        for num in list(maxs.values()):
            power *= num
        total += power

    print(total)


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read().strip().splitlines()
    main(data)
