import time
from re import findall


def parse_input(filename):
    lines = ""
    with open(filename) as inp:
        for line in inp:
            lines = lines + line
    return lines


def find_all_multiplication(parsed_input):
    multiplications_list = [(int(a), int(b)) for a, b in [x.strip("mul()").split(",") for x in findall("mul\(\d+,\d+\)", parsed_input)]]
    return multiplications_list


def main(filename):
    start_time = time.time_ns()
    sum_all = 0
    version = "test" if filename.find("short") > 0 else "puzzle input"

    # parse input
    parsed_input = parse_input(filename)
    print(f"parsed input: {parsed_input}")
    multiplications_list = find_all_multiplication(parsed_input)
    print(f"multiplications_list: {multiplications_list}")
    for multiplication in multiplications_list:
        sum_all += multiplication[0] * multiplication[1]

    print(f"Sum of multiplications {version}: {sum_all}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))


main("input/day03_short.txt")
main("input/day03.txt")
