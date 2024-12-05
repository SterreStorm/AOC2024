import time
from math import floor

def parse_input(filename):
    with open(filename) as inp:
        puzzle_input = inp.read().split("\n\n")
        comparisons =  [[int(z) for z in y.split("|")] for y in [x for x in puzzle_input[0].split("\n")]]
        arrays_to_check = [[int(z) for z in y.split(",")] for y in [x for x in puzzle_input[1].split("\n")]]
    return comparisons, arrays_to_check


def comparisons_to_dict(comparisons):
    numbers_dict = {x: [] for x in set([y[0] for y in comparisons])}
    for doubles in comparisons:
        value = numbers_dict[doubles[0]]
        value.append(doubles[1])
        numbers_dict[doubles[0]] = value
    return numbers_dict


def check(check_array, comparisons_dict):
    check_number_location = 0
    for check_number_location, check_number in enumerate(check_array):
        if check_number in comparisons_dict:
            ahead_array = comparisons_dict[check_number]
            for number_ahead in ahead_array:
                if number_ahead in check_array and check_array.index(number_ahead) < check_number_location:
                    return False, check_number_location
    return True, check_number_location


def reorder_array(array, wrong_location, comparisons_dict):
    in_wrong_place = array.pop(wrong_location)
    must_be_behind = comparisons_dict[in_wrong_place]
    for location in range(0, wrong_location):
        if array[location] in must_be_behind:
            array.insert(location, in_wrong_place)
            correct, new_location = check(array, comparisons_dict)
            return array if correct else reorder_array(array, new_location, comparisons_dict)


def total_middle_correct(arrays, comparisons_dict):
    sum_middle_correct = 0
    sum_middle_incorrect = 0
    for array in arrays:
        correct, location = check(array, comparisons_dict)
        if correct:
            sum_middle_correct += array[floor(len(array) / 2)]
        else:
            array = reorder_array(array, location, comparisons_dict)
            sum_middle_incorrect += array[floor(len(array) / 2)]
    return sum_middle_correct, sum_middle_incorrect


def main(filename):
    start_time = time.time_ns()
    version = "test input" if filename.find("short") > 0 else "puzzle input"
    # parse input
    comparisons, arrays_to_check = parse_input(filename)
    comparisons_dict = comparisons_to_dict(comparisons)


    # pt 1, pt2
    sum_middle_correct, sum_middle_incorrect = total_middle_correct(arrays_to_check, comparisons_dict)

    print(f"sum middle correct {version}: {sum_middle_correct}")
    print(f"sum middle reordered incorrect {version}: {sum_middle_incorrect}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

main("input/day05_short.txt")
main("input/day05.txt")
