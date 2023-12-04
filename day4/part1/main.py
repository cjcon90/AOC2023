from pathlib import Path


def get_score(winning_numbers):
    if not len(winning_numbers):
        return 0
    if len(winning_numbers) == 1:
        return 1
    return 2 * get_score(winning_numbers[1:])


def check_tickets(data):
    if not len(data):
        return 0
    game = data[0]
    winning = sorted(game.split(":")[1].split("|")[0].strip().split())
    mine = sorted(game.split("|")[1].strip().split())
    winning_numbers = [n for n in mine if n in winning]
    score = get_score(winning_numbers)
    return score + check_tickets(data[1:])


def main(data):
    print(check_tickets(data))


if __name__ == "__main__":
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        data = f.read().strip().splitlines()
    main(data)
