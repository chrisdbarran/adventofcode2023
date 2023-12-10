from colorama import Fore, Style
# looks like a maze problem, find the manhattan distance to each tile
# Furthest one is the one with the largest distance
# need to make sure we know if we've seen the tile before.
# Assumtion is that it always forms a loop from the start.

# in a NESW config
VALID = {
    'S': ("|F7", "-J7","|JL", "-FL"),
    'F': ("","-7J","|JL",""),
    "7": ("","","|JL","-FL"),
    "L": ("|7F", "7J-","",""),
    "J": ("F|7", "","","-FL"),
    "-": ("","J-7","","F-L"),
    "|": ("F7|","","LJ|","")
}

class Node:

    def __init__(self, type, location):
        self.type = type
        self.location = location
        self.outgoing = []
        self.visited = False

    def add_edge(self, edge):
        self.outgoing.append(edge)

    def get_next_node(self, grid):
        if self.type == 'S':
            # just return the first one
            return grid[self.outgoing[0]]
        nodes = [ grid[x] for x in self.outgoing if not grid[x].visited]
        return nodes[0] if nodes else None

    def __str__(self):
        return f"Type: {self.type}, Location: {self.location}, Outgoing: {self.outgoing}, Visited: {self.visited}"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.location)

def load_data(filename):
    grid = {}
    start = None
    with open(filename, 'r') as f:
        for r, line in enumerate(f.readlines()):
            for c, type in enumerate(line.strip()):
                node = Node(type, (r,c))
                grid[(r,c)] = node
                if type == 'S':
                    start = (r, c)
        shape = (r, c)
    return (start, grid, shape)

def add_edges(grid, shape):
    for location, node in grid.items():
        # Can only traverse horizontal and vertical 1 step
        # will need to check edge conditions
        if node.type == '.':
            continue
        r, c = node.location
        # North
        if r > 0 and grid[(r - 1,c)].type in VALID[node.type][0]:
            node.add_edge((r - 1,c))
        # South
        if r < shape[0] and grid[(r + 1, c)].type in VALID[node.type][2]:
            node.add_edge((r + 1, c))
        # East
        if c < shape[1] and grid[(r, c + 1)].type in VALID[node.type][1]:
            node.add_edge((r, c + 1))
        # West
        if c > 0 and grid[(r, c - 1)].type in VALID[node.type][3]:
            node.add_edge((r, c - 1))

def build_route(current_node, grid):
    visited = []
    while current_node and current_node.visited is False:
        current_node.visited = True
        visited.append(current_node)
        current_node = current_node.get_next_node(grid)
    return visited

def show_route(shape, grid):
    for r in range(0, shape[0]):
        row = ''
        for c in range(0, shape[1]):
            node = grid[(r,c)]
            if node.visited:
                row += f"{Fore.RED}{node.type}{Style.RESET_ALL}"
            else:
                row += grid[(r,c)].type
        print(row)


def find_shortest_route(filename):
    start, grid , shape = load_data(filename)
    add_edges(grid, shape)
    initial = grid[start]
    print(initial)
    visited = build_route(initial, grid)
    show_route(shape, grid)
    return int(len(visited) / 2)

test = find_shortest_route('./day10/part1-test-input.txt')
print(f"Test: {test}")
assert test == 4

test2 = find_shortest_route('./day10/part1-test2-input.txt')
print(f"Test2: {test2}")
assert test2 == 8

test3 = find_shortest_route('./day10/part1-test3-input.txt')
print(f"Test3: {test3}")
assert test3 == 6

result = find_shortest_route('./day10/input.txt')
print(f"Result: {result}")