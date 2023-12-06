import time
from functools import reduce

def load_races(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith("Time:"):
                times = [int(x) for x in line.replace('Time:','').strip().split()]
            if line.startswith("Distance:"):
                distances = [int(x) for x in line.replace('Distance:','').strip().split()]

    races = zip(times, distances)
    return races

def find_winners(race):
    t, s = race
    count = 0
    for v in range(0, t + 1, 1):
        if (v * (t - v)) > s:
            count += 1
    return count

def race_boats(races):
    results = []
    for race in races:
        tic = time.perf_counter()
        results.append(find_winners(race))
        toc = time.perf_counter()
        print(f"Test ran in  {toc - tic:0.4f} seconds")
    result = reduce(lambda x, y: x*y, results)
    return result

test_races = load_races('./day6/part1-test-input.txt')
assert race_boats(test_races) == 288

races = load_races('./day6/input.txt')
print(race_boats(races))