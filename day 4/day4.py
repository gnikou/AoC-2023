from collections import defaultdict


def func(card):
    card_no = int(card.split(":")[0].strip().split()[-1])
    card_possesion[card_no] += 1
    ours = card.split(":")[1].strip().split("|")[0].strip().split()
    ours = [int(i) for i in ours]
    winning = card.split(":")[1].strip().split("|")[1].strip().split()
    winning = set([int(i) for i in winning])
    count = 0
    for num in ours:
        if num in winning:
            count += 1
            for copies in range(card_possesion[card_no]):
                card_possesion[card_no + count] += 1
    if count:
        return 2 ** (count - 1)
    return 0


file = "input_d4"
with open(file) as f:
    cards = f.read().strip().splitlines()
card_possesion = defaultdict(int)
points = sum(map(func, cards))
print(points)
print(sum(card_possesion.values()))
