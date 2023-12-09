import string
from collections import Counter

def game(part, hands, bids):
    cards = Counter()
    crd_value = card_values(part)

    ranks = dict()
    ranking = dict()

    for i, word in zip(string.ascii_uppercase, crd_value):
        ranking[word] = i
    inv_ranking = {v: k for k, v in ranking.items()}

    win_order = []
    for idx, hand in enumerate(hands):
        cards = Counter()

        for card in hand:
            cards.update(card)
        no_dif_cards = len(cards)
        rank = card_rank(no_dif_cards, cards, hand, part)
        ranks[idx] = rank

    # print(ranks)
    for i in range(1, 8):
        r = [hands[k] for k, v in ranks.items() if v == i]
        tmp2 = []
        for item in r:
            tmp = []
            for idx, k in enumerate(item):
                tmp.append(ranking[k])
            tmp2.append(''.join(str(e) for e in tmp))
        sort = sorted(tmp2)

        for idx, k in enumerate(sort):
            tmp3 = []
            tmp4 = []
            for char in k:
                tmp3.append(inv_ranking[char])
            tmp4 = ''.join(str(e) for e in tmp3)
            win_order.append(tmp4)

    s = 0
    for order, hand in enumerate(win_order):
        s += bids[hands.index(hand)] * (order + 1)
    print(s)


def card_values(part):
    return ["J", '2', '3', '4', '5', '6', '7', '8', '9', "T", "Q", "K", "A"] if part == 2 \
        else ['2', '3', '4', '5', '6', '7', '8', '9', "T", "J", "Q", "K", "A"]


def card_rank(no_dif_cards, cards, hand, part):
    if part == 1:
        match no_dif_cards:
            case 1:
                rank = 7
            case 2:
                rank = 6 if 4 in cards.values() else 5
            case 3:
                rank = 4 if 3 in cards.values() else 3
            case 4:
                rank = 2
            case 5:
                rank = 1
    else:
        match no_dif_cards:
            case 1:
                rank = 7
            case 2:
                rank = 6 if 4 in cards.values() else 5
                if hand.count('J'):
                    rank = 7
            case 3:
                rank = 4 if 3 in cards.values() else 3
                if hand.count('J'):
                    if rank == 3:
                        rank += hand.count('J') + 1
                    else:
                        rank = 6
            case 4:
                rank = 2
                if hand.count('J'):
                    rank = 4
            case 5:
                rank = 1
                if hand.count('J'):
                    rank = 2
    return rank


file = "input_d7"
with open(file) as f:
    lines = f.read().strip().splitlines()

hands = [a.split()[0] for a in lines]
bids = [int(a.split()[1]) for a in lines]

game(1, hands, bids)
game(2, hands, bids)
