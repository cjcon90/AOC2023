import re
from pathlib import Path


def beats_record(time: int, distance: int, speed: int) -> bool:
    moving_time = time - speed
    return (speed * moving_time) > distance


def get_win_methods(
    minfail: int,
    start: int,
    maxfail: int,
    end: int,
    time: int,
    distance: int
) -> int:
    startmatch = beats_record(time, distance, start)
    endmatch = beats_record(time, distance, end)
    mid = round(time / 2)
    if (startmatch and endmatch) and (start - 1 == minfail) and (end + 1 == maxfail):
        return end + 1 - start
    if startmatch:
        if start - minfail > 1:
            start = round(start - ((start - minfail) / 2))
    else:
        oldstart = start
        start = start + round((mid - start) / 2)
        minfail = oldstart
    if endmatch:
        if maxfail - end > 1:
            end = end + round((maxfail - end) / 2)
    else:
        oldend = end
        end = end - round((end - mid) / 2)
        maxfail = oldend
    return get_win_methods(minfail, start, maxfail, end, time, distance)


def main(data):
    time_txt, distance_txt = data.strip().split('\n')
    time = int(''.join(re.findall(r'\d+', time_txt)))
    distance = int(''.join(re.findall(r'\d+', distance_txt)))
    start = round(time * 0.25)
    end = round(time * 0.75)
    print(get_win_methods(0, start, time, end, time, distance))


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read()
    main(data)
