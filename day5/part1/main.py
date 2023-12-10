from typing import List
from pathlib import Path
from collections import namedtuple

MAP_NAMES: List[str] = ['seed-to-soil', 'soil-to-fertilizer',
                        'fertilizer-to-water', 'water-to-light',
                        'light-to-temperature', 'temperature-to-humidity',
                        'humidity-to-location']


Map = namedtuple("Map", "destination source length")


def get_seeds(data: str) -> List[int]:
    return [int(num) for num in data.split('seeds:')
            [1].split('\n\n')[0].strip().split()]


def get_map_data(data: str, name: str) -> str:
    return data.split(f'{name} map:')[1].strip().split('\n\n')[0]


def create_map(data: str, map_name: str) -> List[Map]:
    text = get_map_data(data, map_name)
    maps = []
    for line in text.split('\n'):
        destination, source, length = (int(c) for c in line.split(' '))
        maps.append(Map(destination, source, length))
    return maps


def main(data):
    seeds = get_seeds(data)
    maps = {map_name: create_map(data, map_name) for map_name in MAP_NAMES}
    locations = []
    for seed in seeds:
        for map_vals in maps.values():
            for map in map_vals:
                if map.source <= seed <= map.source + map.length:
                    seed = seed + (map.destination - map.source)
                    break
        locations.append(seed)
    print(min(locations))


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read()
    main(data)
