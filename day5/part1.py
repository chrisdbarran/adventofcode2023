
def parse_data(filename):
    seeds = []
    mappings = {}
    with open(filename, 'r') as f:

        current_map = ""
        for line in f.readlines():
            if line.startswith("seeds: "):
                seeds = [int(x) for x in line.split(':')[1].strip().split(' ')]

            elif line.endswith('map:\n'): # start a map
                current_map = line.split()[0]
                mappings[current_map] = []

            elif line == "\n":
                continue

            else:
                mapping = tuple([int(x) for x in line.strip().split()])
                mappings[current_map].append(mapping)
    return (seeds, mappings)

def find_next_id_for_range(source_id, map_range):
    dest_start, source_start, length = map_range
    if source_id >= source_start and source_id <= source_start + length:
        loc = source_id - source_start + dest_start
        if loc > dest_start and loc <= dest_start + length:
            return loc
    raise IndexError(f"{source_id} not in range {map_range}")

assert find_next_id_for_range(79, (52, 50, 48)) == 81

def find_next_id_for_map(current_id, mapping):
    ids = []
    for range in mapping:
        try:
            ids.append(find_next_id_for_range(current_id, range))
        except IndexError as e:
            continue
    if ids:
        return min(ids)
    # not in any range
    return current_id

assert find_next_id_for_map(79, [(50,98,2),(52, 50, 48)]) == 81

# loops over each map to find the next id
def find_location_for_seed(seed, mappings):
    current_id = seed
    for mapping in mappings.values():
        current_id = find_next_id_for_map(current_id, mapping)
    return current_id

def find_lowest_location(filename):
    seeds, mappings = parse_data(filename)
    return min([find_location_for_seed(x, mappings) for x in seeds])


lowest_test = find_lowest_location('./day5/part1-test-input.txt')
print("Lowest test: ", lowest_test)
assert lowest_test == 35

lowest_location = find_lowest_location('./day5/input.txt')
print("Lowest Location: ", lowest_location)