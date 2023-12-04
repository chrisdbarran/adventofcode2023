
def points_total(filename):
    total = 0
    with open(filename, 'r') as f:
        for card in f.readlines():
            card_total = 0
            colon_index = card.index(':')
            pipe_index = card.index('|')

            winning_part = card[colon_index + 1 : pipe_index].strip().split()
            my_part = card[pipe_index + 1:].strip().split()

            winning_numbers = set([int(number) for number in winning_part])
            my_numbers = set([int(number) for number in my_part])

            my_winning_numbers = my_numbers.intersection(winning_numbers)

            if my_winning_numbers:
                card_total = 1 * 2**(len(my_winning_numbers) - 1)

            print("Winning Numbers ", my_winning_numbers,"score: ", card_total)
            total += card_total
    return total

test_total = points_total('./day4/part1-test-input.txt')
print("Test total: ", test_total)
assert test_total == 13


part1_total = points_total('./day4/input.txt')
print("Part1 total: ", part1_total)
