
def total_valid_games(filename):
    total = 0
    with open(filename,'r') as f:
        for line in f.readlines():
            game_id = int(line.split(":")[0].replace("Game ",""))
            rounds = line.strip().split(":")[1].split(';')
            valid = True
            for round in rounds:
                bag = {"red": 12, "green": 13, "blue": 14}
                cubes = round.split(',')
                for cube in cubes:
                    count = int(cube.split(' ')[1])
                    colour = cube.split(' ')[2]
                    if colour in bag:
                        bag[colour] = bag[colour] - count
                    if bag[colour] < 0:
                        valid = False
                        break
            if valid:
                total += game_id
    return total

assert total_valid_games('./day2/part1-test-input.txt') == 8

print("Total test games: ", total_valid_games('./day2/part1-test-input.txt'))
print("Total input: ", total_valid_games('./day2/input.txt'))