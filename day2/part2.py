
def get_fewest_power(filename):
    power = 0
    with open(filename,'r') as f:
        total = 0
        for line in f.readlines():
            rounds = line.strip().split(":")[1].split(';')
            bag = {}
            for round in rounds:
                cubes = round.split(',')
                for cube in cubes:
                    count = int(cube.split(' ')[1])
                    colour = cube.split(' ')[2].strip()
                    if colour in bag:
                        if(count > bag[colour]):
                            bag[colour] = count
                    else:
                        bag[colour] = count
            product = 1
            for colour_count in bag.values():
                product = product * colour_count
            total += product
    return total

assert get_fewest_power('./day2/part1-test-input.txt') == 2286

print("Total test games: ", get_fewest_power('./day2/part1-test-input.txt'))
print("Total input: ", get_fewest_power('./day2/input.txt'))