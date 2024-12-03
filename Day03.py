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


def calculate_multiplications(multiplications_list):
    sum_all = 0
    for multiplication in multiplications_list:
        sum_all += multiplication[0] * multiplication[1]
    return sum_all


def find_exclusion_text(parsed_input):
    current_dont = parsed_input.find("don't()")
    exclusions = ""
    while current_dont != -1:
        current_do = parsed_input.find("do()", current_dont)
        exclusions = exclusions + parsed_input[current_dont:current_do]
        current_dont = parsed_input.find("don't", current_do)
    return exclusions


def main(filename):
    start_time = time.time_ns()
    version = "David" if filename.find("dovob") > 0 else "puzzle input"

    # part 1
    parsed_input = parse_input(filename)
    multiplications_list = find_all_multiplication(parsed_input)
    sum_all = calculate_multiplications(multiplications_list)

    # Veel te lang gedaan over de exclusion vinden met regex, maar gewoon omgeschreven
    #part 2
    exclusions = find_exclusion_text(parsed_input)
    exclusions_list = find_all_multiplication(exclusions)
    sum_exclusions = calculate_multiplications(exclusions_list)

    sum_inclusions = sum_all - sum_exclusions
    print(f"Sum_all - sum_exclusions part 2: {version}: {sum_inclusions}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

main("input/day03.txt")
