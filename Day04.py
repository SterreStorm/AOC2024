import time


def parse_input(filename):
    with open(filename) as inp:
            lines = [line.strip() for line in inp.readlines()]
    return lines


def define_columns(rows):
    grid_columns = [["." for x in range(len(rows))] for y in range(len(rows[0]))]
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            grid_columns[j][i] = rows[i][j]
    grid_columns = ["".join(x) for x in grid_columns]
    return grid_columns


def find_diagonals(rows, columns):
    width = len(columns)
    height = len(rows)
    grid_diagonals_f = ["" for x in range(width + height - 1)]
    grid_diagonals_b = grid_diagonals_f.copy()
    for x in range(width):  # X coordinate
        for y in range(height): # Y coordinate
            grid_diagonals_f[x+y] += rows[y][x]
            grid_diagonals_b[x - y + height - 1] += rows[y][x]
    return grid_diagonals_f, grid_diagonals_b


def sum_word(lines, word):
    appearance_sum = 0
    rev_word = word[::-1]
    for line in lines:
        appearance_sum += line.count(word) + line.count(rev_word)
    return appearance_sum


def sum_mas(rows, word):
    sum_mas = 0
    word_reverse = word[::-1]
    for i in range(1, len(rows) - 1):
        A = word[1]
        row = rows[i][1:-1]
        count = row.count(A)
        if count > 0:
            a_loc = -1
            for j in range(count):
                a_loc = row.find(A, a_loc + 1)
                diagonal_1 = rows[i - 1][a_loc] + A + rows[i + 1][a_loc + 2]
                diagonal_2 =  rows[i - 1][a_loc + 2] + A + rows[i + 1][a_loc]
                sum_mas += 1 if ((diagonal_1 == word or diagonal_1 == word_reverse) and (diagonal_2 == word or diagonal_2 == word_reverse)) else 0
    return sum_mas


def main(filename, word):
    start_time = time.time_ns()
    version = "test input" if filename.find("short") > 0 else "puzzle input"

    # parse input
    grid_rows = parse_input(filename)
    grid_columns = define_columns(grid_rows)
    grid_diagonals_b, grid_diagonals_f= find_diagonals(grid_rows, grid_columns)

    # part 1
    all_rows = grid_rows + grid_columns + grid_diagonals_f + grid_diagonals_b
    sum_words = sum_word(all_rows, "X" + word)
    print(f"sum part 1 {version}: {sum_words}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

    # part 2
    sum_xmas = sum_mas(grid_rows, word)

    print(f"sum part 2 {version}: {sum_xmas}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))


main("input/day04.txt", "MAS")
