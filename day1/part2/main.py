import re
from pathlib import Path


WORDNUMS = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
WORDREG = re.compile('|'.join(WORDNUMS.keys()))
ALLREG = re.compile('|'.join(list(WORDNUMS.keys()) +
                    list(str(num) for num in WORDNUMS.values())))


def _word_to_num(line: str) -> str:
    for word in WORDREG.findall(line):
        line = line.replace(word, str(WORDNUMS[word]))
    return line


def main(data):
    total = 0
    for line in data:
        all = ALLREG.findall(line)
        value = f"{all[0]}{all[-1]}"
        total += int(_word_to_num(value))
    print(total)


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read().splitlines()
    main(data)
