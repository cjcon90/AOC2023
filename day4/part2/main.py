import re
from pathlib import Path
import asyncio

CARD_REG = re.compile(r"Card\s+(\d+)\:\s*([\d\s]+)\s*\|\s*([\d\s]+)")


async def main(data):

    datadict = {}
    for line in data:
        card, winning, mine = CARD_REG.match(line).groups()
        datadict[int(card)] = (winning, mine)

    total_tickets = {k: 1 for k in datadict.keys()}
    current = 1
    while current < len(data):
        winning, mine = (sorted(x.split()) for x in datadict[current])
        winning_numbers = [n for n in mine if n in winning]
        score = len(winning_numbers)
        won = [current + n for n in range(1, score + 1)]
        num_won = total_tickets[current]
        for ticket in won:
            total_tickets[ticket] += num_won
        current += 1

    print(sum(total_tickets.values()))


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read().strip().splitlines()
    asyncio.run(main(data))
