# "ja laten we alles netjes een eigen functie geven dat is vast handig"

def parse_input(filename):
    with open(filename) as inp:
        list1 = []
        list2 = []
        for line in inp:
            pos1, pos2 = line.split()
            list1.append(int(pos1))
            list2.append(int(pos2))
        return list1, list2


def sort_list(list1, list2):
    list1.sort()
    list2.sort()
    return list1, list2


def calculate_distance(list1, list2):
    distance = 0
    for i, value in enumerate(list1):
        distance += abs(value - list2[i])
    return distance


def find_similarity_score(list1, list2):
    similarity_score = 0
    for value in list2:
        similarity_score += value * list1.count(value)
    return similarity_score

def main(filename):
    if filename.find("short") > 0:
        version = "test input"
    else:
        version = "actual input"

    # pt 1
    list1, list2 = parse_input(filename)
    list1, list2 = sort_list(list1, list2)
    distance = calculate_distance(list1, list2)
    print(f"distance {version}: {distance}")
    # pt 2
    similarity_score = find_similarity_score(list1, list2)
    print(f"similarity score {version}: {similarity_score}")


main("input/day01_short.txt")
main("input/day01.txt")