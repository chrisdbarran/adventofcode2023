from collections import Counter

TYPES = {
    (1,1,1,1,1) : 0,
    (2,1,1,1) : 1,
    (2,2,1) : 2,
    (3,1,1) : 3,
    (3,2) : 4,
    (4,1) : 5,
    (5,) : 6
}

CARDS = "23456789TJQKA"

class Hand:

    def __init__(self, hand, bid):
        self.hand = list(hand)
        self.bid = bid
        self.type = self.infer_type()

    def infer_type(self):
        counter = tuple(sorted(Counter(self.hand).values(), reverse=True))
        return TYPES[counter]

    def __str__(self):
        return f"{self.hand}, {self.type}, {self.bid}"

    def __lt__(self, other):
        if self.type == other.type:
            pairs = zip(self.hand, other.hand)
            for self_card, other_card in pairs:
                if self_card == other_card:
                    continue
                else:
                    return CARDS.index(self_card) < CARDS.index(other_card)
        return self.type < other.type

def load_hands(filename):
    hands = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            hand, bid = line.strip().split(' ')
            hands.append(Hand(hand, int(bid)))
    return hands

def sort_hands(hands):
    return sorted(hands, reverse=False)

def calculate_winnings(hands):
    winnings = 0
    for rank, hand in enumerate(hands):
        print(rank + 1 , hand)
        winnings += ((rank + 1) * hand.bid)
    return winnings

def part1(filename):
    return calculate_winnings(sort_hands(load_hands(filename)))

assert  Hand('KTJJT',1) < Hand('KK677',1)

test_winnings = part1('./day7/part1-test-input.txt')
print(f"Test Winnings: {test_winnings}")
assert test_winnings == 6440

winnings = part1('./day7/input.txt')
print(winnings)