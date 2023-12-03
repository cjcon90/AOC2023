import re
from typing import List, Tuple
from pathlib import Path

SYMBOLREG = re.compile(r"[*]")
NUMREG = re.compile(r"\d+")


def get_symbol_locations(idx, row) -> List[int]:
    return [f"{idx}:{match.start()}" for match in SYMBOLREG.finditer(row)]


def get_row_num_locations(row) -> List[Tuple[int, int]]:
    return [(match.start(), match.end()) for match in NUMREG.finditer(row)]


def get_adjacent(idx, number, symbol_locations) -> List[str]:
    touchpoints = []
    for x in range(-1, 2):
        for y in range(number[0] - 1, number[1] + 1):
            touchpoints.append(f"{idx + x}:{y}")
    return [pos for pos in touchpoints if pos in symbol_locations]


def main(data):
    symbol_locations = []
    for idx, row in enumerate(data):
        symbol_locations.extend(get_symbol_locations(idx, row))

    gears = {}
    for idx, row in enumerate(data):
        number_locations = get_row_num_locations(row)
        for number in number_locations:
            if adj := get_adjacent(idx, number, symbol_locations):
                for gear in adj:
                    gears[gear] = gears.get(
                        gear, []) + [data[idx][number[0]:number[1]]]

    total = 0
    for gear, numbers in gears.items():
        if len(numbers) == 2:
            total += int(numbers[0]) * int(numbers[1])

    print(total)


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read().strip().splitlines()
    main(data)
