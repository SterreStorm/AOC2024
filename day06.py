import time
from collections import Counter

def parse_input(filename):
    with open(filename) as inp:
            lines = [list(line.strip()) for line in inp.readlines()]
    return lines


def find_start(grid):
    for y, row in enumerate(grid):
        if "^" in row:
            x = row.index("^")
            return x, y


def traverse_grid(grid, start):
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    width = len(grid[0])
    height = len(grid)
    new_x, new_y = start

    turns = 0
    dir_x, dir_y = directions[turns % len(directions)]

    while -1 < new_x < width and -1 < new_y < height:
        if grid[new_y][new_x] == "#":
            turns += 1
            dir_x, dir_y = directions[turns % len(directions)]
            new_x, new_y = [curr_x + dir_x, curr_y + dir_y]
        else:
            curr_x, curr_y = new_x, new_y
            grid[curr_y][curr_x] = "x"
            new_x, new_y = [curr_x + dir_x, curr_y + dir_y]
    return grid



def main(filename):
    start_time = time.time_ns()
    version = "test input" if filename.find("short") > 0 else "puzzle input"

    # parse input
    grid = parse_input(filename)
    start_x, start_y = find_start(grid)
    traversed_grid = traverse_grid(grid, [start_x, start_y])

    # pt 1
    count_x = 0
    for row in traversed_grid:
        count_x += row.count("x") if "x" in row else 0
    print(f"steps {version}: {count_x}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

main("input/day06_short.txt")
main("input/day06.txt")
