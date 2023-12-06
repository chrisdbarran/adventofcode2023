import time

class SeedMapper:

    def __init__(self, filename):
        self.filename = filename
        self.seeds, self.mappings = self.parse_data()

    def parse_data(self):
        seeds = []
        mappings = {}
        with open(self.filename, 'r') as f:

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

    def find_next_id_for_range(self, source_id, map_range):
        dest_start, source_start, length = map_range
        if source_id >= source_start and source_id <= source_start + length:
            loc = source_id - source_start + dest_start
            if loc >= dest_start and loc <= dest_start + length:
                return loc
        return -1

    # Is the first one always the lowest?
    def find_next_id_for_map(self, current_id, map_name, mapping):
        for range in mapping:
            id = self.find_next_id_for_range(current_id, range)
            if id != -1:
                return id
        return current_id

    def test_next_id_for_map(self, map_name, seed, ranges, expected):
        actual = self.find_next_id_for_map(seed, map_name, ranges)
        print(f"{map_name:<25} seed: {seed:<5} expected: {expected:<5} actual: {actual:<5}")

    # loops over each map to find the next id
    def find_location_for_seed(self, seed):
        current_id = seed
        for map_name, mapping in self.mappings.items():
            current_id = self.find_next_id_for_map(current_id, map_name, mapping)
        return current_id

#   ´soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46.
    def test_find_location_for_seed(self):
        loc = self.find_location_for_seed(82)
        print("Test find_location_for_seed(82), expected 46, actual ", loc )
        #assert loc == 46

    def process_seeds(self, seeds):
        starts = seeds[::2]
        lengths = seeds[1::2]
        return list(zip(starts, lengths))

    def find_lowest_location(self):
        seed_tuples = self.process_seeds(self.seeds)
        location = None
        for seed_tuple in seed_tuples:
            for seed in range(seed_tuple[0], sum(seed_tuple)):
                loc = self.find_location_for_seed(seed)
                if location == None or location > loc:
                    location = loc
        return location

tic = time.perf_counter()
test_mapper = SeedMapper('./day5/part1-test-input.txt')
lowest_test = test_mapper.find_lowest_location()
print("Lowest test: ", lowest_test)
assert lowest_test == 46
toc = time.perf_counter()
print(f"Test ran in  {toc - tic:0.4f} seconds")

test_mapper.test_next_id_for_map("seed-to-soil", 82, [(50,98,2),(52, 50, 48)], 84)
test_mapper.test_next_id_for_map("soil-to-fertilizer", 84, [(0,15,37),(37, 52, 2),(39, 0, 15)], 84)
test_mapper.test_next_id_for_map("fertilizer-to-water", 84, [(49, 53, 8),(0, 11, 42), (42, 0, 7), (57, 7, 4)], 84)
test_mapper.test_next_id_for_map("water-to-light", 84, [(88, 18, 7),(18, 25, 70)], 77)
test_mapper.test_next_id_for_map("light-to-temperature", 77, [(45, 77, 23),(81, 45, 19),(68, 64,13)], 45)
test_mapper.test_next_id_for_map("temperature-to-humidity", 45, [(0, 69, 1),(1, 0, 69)], 46)
test_mapper.test_next_id_for_map("humidity-to-location", 46, [(60, 56, 37),(56, 93, 4)], 46)


# tic = time.perf_counter()
# mapper = SeedMapper('./day5/input2.txt')
# lowest_location = mapper.find_lowest_location()
# print("Lowest Location: ", lowest_location)
# toc = time.perf_counter()
# print(f"Part2 ran in  {toc - tic:0.4f} seconds")