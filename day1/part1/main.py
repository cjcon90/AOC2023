import re
from pathlib import Path


def main():
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read().splitlines()

    total = 0
    for line in data:
        nums = ''.join(re.findall(r"\d+", line))
        if not nums:
            continue
        total += (int(f"{nums[0]}{nums[-1]}"))
    print(total)


if __name__ == "__main__":
    main()
