import time
from functools import reduce

def load_race(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line.startswith("Time:"):
                time = int(''.join(line.replace('Time:','').strip().split()))
            if line.startswith("Distance:"):
                distance = int(''.join(line.replace('Distance:','').strip().split()))
    race = (time, distance)
    return race

def find_winners(race):
    t, s = race
    count = 0
    for v in range(0, t + 1, 1):
        if (v * (t - v)) > s:
            count += 1
    return count

def race_boats(race):
    results = []
    tic = time.perf_counter()
    results.append(find_winners(race))
    toc = time.perf_counter()
    print(f"Test ran in  {toc - tic:0.4f} seconds")
    result =  reduce(lambda x, y: x*y, results)
    return result

test_race = load_race('./day6/part1-test-input.txt')
print(test_race)
assert race_boats(test_race) == 71503

race = load_race('./day6/input.txt')
print(race_boats(race))
