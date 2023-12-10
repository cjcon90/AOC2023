from typing import List, Dict
from pathlib import Path
from collections import namedtuple

MAP_NAMES: List[str] = ['seed-to-soil', 'soil-to-fertilizer',
                        'fertilizer-to-water', 'water-to-light',
                        'light-to-temperature', 'temperature-to-humidity',
                        'humidity-to-location']


Map = namedtuple("Map", "destination source length")


def get_seed_ranges(data: str) -> List[int]:
    text = data.split('seeds:')[1].split('\n\n')[0].strip()
    nums = [int(num) for num in text.split()]
    ranges = []
    for i in range(0, len(nums), 2):
        ranges.append(range(nums[i], nums[i] + nums[1]))
    return ranges


def get_map_data(data: str, name: str) -> str:
    return data.split(f'{name} map:')[1].strip().split('\n\n')[0]


def get_map_ranges(data: str, map_name: str) -> Dict[range, range]:
    text = get_map_data(data, map_name)
    ranges = {}
    for line in text.split('\n'):
        destination, source, length = (int(c) for c in line.split(' '))
        ranges[range(source, source + length)
               ] = range(destination, destination + length)
    return ranges


def main(data):
    map_ranges = {map_name: get_map_ranges(
        data, map_name) for map_name in MAP_NAMES}
    seed_ranges = get_seed_ranges(data)
    location = 0
    while True:
        value = location
        for map, map_range in reversed(map_ranges.items()):
            for source, dest in map_range.items():
                if value in dest:
                    change = source.start - dest.start
                    value += change
                    break
        if any(value in seed_range for seed_range in seed_ranges):
            print(location)
            return
        location += 1


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read()
    main(data)
