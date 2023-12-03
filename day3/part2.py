# A number adjacent to a symbol even diagonallly is a part number
# . is not a symbol
# add up all the part numbers
import math

num_chars = "0123456789"
not_symbols = num_chars + "."
print_matches = False


def missing_part(filename):
    gears = {}
    grid = []
    numbers = []

    with open(filename, 'r') as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    # find numbers and symbols
    for row in range(0, len(grid)):
        num = []
        for col in range(0, len(grid[row])):
            char = grid[row][col]
            if char in num_chars:
                num.append(char)

            # char is a . or a symbol or end of line signifying possible end of number
            if char not in num_chars or (col + 1 == len(grid[row])):
                if num:
                    number = ''.join(num)
                    num = []
                    # We've found a number
                    # Check if it's adjacent to a symbol
                    row_min = row - 1 if row - 1 > 0 else 0
                    row_max = row + 2 if row + 2 < len(grid) else len(grid)
                    col_min = col - len(number) - 1 if col - len(number) - 1 > 0 else 0
                    col_max = col + 1 if col + 1 < len(grid[row]) else len(grid[row])

                    match = False
                    temp = ""
                    for i in range(row_min, row_max):
                        for j in range(col_min, col_max):
                            temp = temp + grid[i][j]
                            if grid[i][j] == '*':
                                if (i,j) in gears.keys():
                                    gears[(i,j)].append(int(number))
                                else:
                                    gears[(i,j)] = [int(number)]
                                match = True
                        temp = temp + "\n"
                    if match and print_matches:
                        print(temp)
    for gear in gears.values():
        if len(gear) == 2:
            numbers.append(math.prod(gear))
            print(gear)

    return sum(numbers)

mp_test = missing_part('./day3/part1-test-input.txt')
assert mp_test == 467835
print("Missing part test: ", mp_test)

input1 = missing_part('./day3/input1.txt')
print("Missing part input1: ", input1)
assert input1 == 6756

print("Missing part: ", missing_part('./day3/input.txt'))