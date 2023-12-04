print_cards = False

def pick_cards(index, deck, indent):
    card, card_count = deck[index]

    if print_cards:
       print(" "*indent, card)

    indent += 2
    pick_cards.counter += 1
    
    for i in range(index + 1, index + card_count + 1):
         pick_cards(i, deck, indent)

def count_scratchcards(filename):
    deck = []
    with open(filename, 'r') as f:
        for card in f.readlines():

            colon_index = card.index(':')
            pipe_index = card.index('|')
            card_id = card[:colon_index]

            winning_part = card[colon_index + 1 : pipe_index].strip().split()
            my_part = card[pipe_index + 1:].strip().split()

            winning_numbers = set([int(number) for number in winning_part])
            my_numbers = set([int(number) for number in my_part])

            my_winning_numbers = my_numbers.intersection(winning_numbers)
            deck.append((card_id, len(my_winning_numbers)))

    pick_cards.counter = 0

    for i in range (0, len(deck)):
        pick_cards(i, deck, 2)
    return pick_cards.counter



test_total = count_scratchcards('./day4/part1-test-input.txt')
print("Test total: ", test_total)
assert test_total == 30


part1_total = count_scratchcards('./day4/input.txt')
print("Part1 total: ", part1_total)
