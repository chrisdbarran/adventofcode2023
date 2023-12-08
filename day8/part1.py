
def parse_data(filename):
    nodes = {}
    with open(filename, 'r') as f:
        steps = [int(x) for x in f.readline().strip().replace('R','1').replace('L','0')]
        f.readline()
        for line in f.readlines():
            key, values = line.strip().split(' = ')
            values = values.replace('(','').replace(')','').split(', ')
            nodes[key] = (values[0], values[1])
    return (steps, nodes)

def follow_map(steps, nodes):
    current_node = 'AAA'
    count = 0

    while current_node != 'ZZZ':
        for step in steps:
            count += 1
            current_node = nodes[current_node][step]
            if current_node == 'ZZZ':
                break
    return count

def count_steps(filename):
    steps, nodes = parse_data(filename)
    return follow_map(steps, nodes)


test_steps = count_steps('./day8/part1-test-input.txt')
print(f"Test steps: {test_steps}")
assert test_steps == 2

steps = count_steps('./day8/input.txt')
print(f"Part1 Steps: {steps}")