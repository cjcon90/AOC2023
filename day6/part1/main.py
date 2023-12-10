import re
import math
from pathlib import Path


def beats_record(time: int, distance: int, speed: int) -> bool:
    moving_time = time - speed
    return (speed * moving_time) > distance


def get_win_methods(start: int, end: int, time: int, distance: int) -> int:
    startmatch = beats_record(time, distance, start)
    endmatch = beats_record(time, distance, end)
    if startmatch and endmatch:
        return end + 1 - start
    if not startmatch:
        start += 1
    if not endmatch:
        end -= 1
    return get_win_methods(start, end, time, distance)


def main(data):
    time_txt, distance_txt = data.strip().split('\n')
    times = re.findall(r'\d+', time_txt)
    distances = re.findall(r'\d+', distance_txt)
    win_methods = []
    for i in range(len(times)):
        time = int(times[i])
        distance = int(distances[i])
        win_methods.append(get_win_methods(1, time - 1, time, distance))

    print(math.prod(win_methods))


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read()
    main(data)
