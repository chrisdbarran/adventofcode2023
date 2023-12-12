import itertools

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
            if '#' not in row:
                universe.append(list(row.strip()))
            universe.append(list(row.strip()))

    transposed = list(map(list, zip(*universe)))
    expanded = []
    for row in transposed:
        if '#' not in row:
            expanded.append(row)
        expanded.append(row)

    return list(map(list, zip(*expanded)))

def find_galaxies(universe):
    galaxies = []
    for r, row in enumerate(universe):
        for c, type in enumerate(row):
            if type == '#':
                galaxy = Galaxy((r,c))
                galaxies.append(galaxy)
    return galaxies



def calculate_result(filename):
    universe = load_data(filename)
    galaxies = find_galaxies(universe)

    results = []
    for a, b in itertools.combinations(galaxies,2):
        results.append(a.manhattan_distance(b))
    return sum(results)


test_result = calculate_result('./day11/part1-test-input.txt')
print(f"Test result: {test_result}")
assert test_result == 374

result = calculate_result('./day11/input.txt')
print(f"Result: {result}")