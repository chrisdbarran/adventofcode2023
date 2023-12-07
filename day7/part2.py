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

CARDS = "J23456789TQKA"

class Hand:

    def __init__(self, hand, bid):
        self.hand = list(hand)
        self.bid = bid
        self.type = self.infer_type()
        self.wild_type = self.infer_wildtype()

    def infer_wildtype(self):
        counts = Counter(self.hand)
        if 'J' in counts.keys():
            num_jokers = counts['J']
            if num_jokers != 5:
                del(counts['J'])
                max_card = max(counts, key=counts.get)
                counts[max_card] += num_jokers
        counter = tuple(sorted(counts.values(), reverse=True))
        return TYPES[counter]

    def infer_type(self):
        counter = tuple(sorted(Counter(self.hand).values(), reverse=True))
        return TYPES[counter]

    def __str__(self):
        return f"Hand: {self.hand}, Type: {self.type}, WildType: {self.wild_type}, Bid: {self.bid}"

    def __lt__(self, other):
        if self.wild_type == other.wild_type:
            pairs = zip(self.hand, other.hand)
            for self_card, other_card in pairs:
                if self_card == other_card:
                    continue
                else:
                    return CARDS.index(self_card) < CARDS.index(other_card)
        return self.wild_type < other.wild_type

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
        winnings += ((rank + 1) * hand.bid)
    return winnings

def part2(filename):
    return calculate_winnings(sort_hands(load_hands(filename)))

# print(Hand('KTJJT',1))
# print(Hand('KK677',1))

test_winnings = part2('./day7/part1-test-input.txt')
print(f"Test Winnings: {test_winnings}")
assert test_winnings == 5905

winnings = part2('./day7/input.txt')
print(winnings)