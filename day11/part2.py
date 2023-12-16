import itertools
from math import exp

class Galaxy:

    def __init__(self, location):
        self.location = location

    def __str__(self):
        return f"{self.location}"

    def __repr__(self):
        return self.__str__()

    def manhattan_distance(self, other):
        return abs(self.location[0] - other.location[0]) + abs(self.location[1] - other.location[1])

def load_data(filename):
    universe = []
    with open(filename, 'r') as f:
        for row in f.readlines():
            universe.append(list(row.strip()))
    return universe

def find_blanks(universe):
    blank_rows = []
    blank_cols = []
    for r, row in enumerate(universe):
        if '#' not in row:
            blank_rows.append(r)
    transposed = list(map(list, zip(*universe)))
    for c, col in enumerate(transposed):
        if '#' not in col:
            blank_cols.append(c)
    return (blank_rows, blank_cols)

def expand(coord, blanks, expansion_factor):
    b = [blank for blank in blanks if blank < coord]
    result = ((len(b)) *(expansion_factor - 1)) + coord
    return result

def find_galaxies(universe, blank_rows, blank_cols, expansion_factor):
    galaxies = []
    for r, row in enumerate(universe):
        for c, type in enumerate(row):
            if type == '#':
                new_row = expand(r, blank_rows, expansion_factor)
                new_col = expand(c, blank_cols, expansion_factor)
                galaxy = Galaxy((new_row, new_col))
                galaxies.append(galaxy)
    return galaxies



def calculate_result(filename, expansion_factor):
    universe = load_data(filename)
    blank_rows, blank_cols = find_blanks(universe)
    galaxies = find_galaxies(universe, blank_rows, blank_cols, expansion_factor)

    results = []
    for a, b in itertools.combinations(galaxies,2):
        results.append(a.manhattan_distance(b))
    return sum(results)


test_result = calculate_result('./day11/part1-test-input.txt', 10)
print(f"Test result: {test_result}")
assert test_result == 1030

test_result = calculate_result('./day11/part1-test-input.txt', 100)
print(f"Test result: {test_result}")
assert test_result == 8410

result = calculate_result('./day11/input.txt', 1000000)
print(f"Result: {result}")