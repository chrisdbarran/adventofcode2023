import math

def parse_data(filename):
    nodes = {}
    paths = []
    with open(filename, 'r') as f:
        steps = [int(x) for x in f.readline().strip().replace('R','1').replace('L','0')]
        f.readline()
        for line in f.readlines():
            key, values = line.strip().split(' = ')
            values = values.replace('(','').replace(')','').split(', ')
            nodes[key] = (values[0], values[1])
            if key.endswith('A'):
                paths.append(key)
    return (steps, nodes, paths)

def not_complete(paths):
    for path in paths:
        if path.endswith('Z'):
            continue
        else:
            return True
    return False

def complete(paths):
    return not not_complete(paths)

debug = False
def follow_map(steps, nodes, paths):
    results = {}
    for path in paths:
        count = 0
        while(not path.endswith('Z')):
            for step in steps:
                count += 1
                path = nodes[path][step]
        results[path] = count
    print(results)
    return math.lcm(*results.values())

def count_steps(filename):
    steps, nodes, paths = parse_data(filename)
    return follow_map(steps, nodes, paths)


test_steps = count_steps('./day8/part2-test-input.txt')
print(f"Test steps: {test_steps}")
assert test_steps == 6

steps = count_steps('./day8/input.txt')
print(f"Part1 Steps: {steps}")