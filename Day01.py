# "ja laten we alles netjes een eigen functie geven dat is vast handig"

import time

def parse_input(filename):
    with open(filename) as inp:
        left_list = []
        right_list = []
        for line in inp:
            pos1, pos2 = line.split()
            left_list.append(int(pos1))
            right_list.append(int(pos2))
        return left_list, right_list


def sort_list(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return left_list, right_list


def calculate_distance(left_list, right_list):
    distance = 0
    for i, value in enumerate(left_list):
        distance += abs(value - right_list[i])
    return distance


def find_similarity_score(left_list, right_list):
    similarity_score = 0
    for value in right_list:
        similarity_score += value * left_list.count(value)
    return similarity_score

def main(filename):
    start_time = time.time_ns()
    if filename.find("short") > 0:
        version = "test input"
    else:
        version = "actual input"

    # pt 1
    left_list, right_list = parse_input(filename)
    left_list, right_list = sort_list(left_list, right_list)
    distance = calculate_distance(left_list, right_list)
    print(f"distance {version}: {distance}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))
    # pt 2
    similarity_score = find_similarity_score(left_list, right_list)
    print(f"similarity score {version}: {similarity_score}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))

main("input/day01_short.txt")
main("input/day01.txt")