import copy
import time


def find_version(filename):
    # meuk voor print statements
    if filename.find("short") > 0:
        version = "test input"
    else:
        version = "actual input"
    return version

def parse_input(filename):
    with open(filename) as inp:
        reports = []
        for line in inp:
            report = line.split()
            report = [int(number) for number in report]
            reports.append(report)
    return reports


def report_safe(report):
    safe = False
    decreasing = (report[0] - report[-1] > 0)
    for i in range(len(report) - 1):
        delta = report[i] - report[i + 1]
        delta_decreasing = delta > 0
        if 3 < abs(delta) or abs(delta) < 1 or delta_decreasing != decreasing:
            return safe
    safe = True
    return safe


def report_safe_dampener(report):
    safe = report_safe(report)
    if not safe:
        decreasing = (report[0] - report[-1] > 0)
        skips = 0
        zipped = zip(report, report[2:])
        for item in zipped:
            pos1, pos2 = item
            delta = pos1 - pos2
            delta_decreasing = delta > 0
            if 3 < abs(delta) or abs(delta) < 1 or delta_decreasing != decreasing:
                skips += 1
        safe = skips < 2
    return safe


def report_safe_combined(report, dampener=False):
    safe = False
    report_copy = report.copy()
    decreasing = (report[0] - report[-1] > 0)
    for i in range(len(report) - 1):
        delta = report[i] - report[i + 1]
        delta_decreasing = delta > 0
        if 3 < abs(delta) or abs(delta) < 1 or delta_decreasing != decreasing:
            if not dampener:
                return safe
            report_copy.pop(i + 1)
            report.pop(i)
            return report_safe_combined(report) or report_safe_combined(report_copy)
    safe = True
    return safe



def main(filename):
    # variables
    start_time = time.time_ns()
    version = find_version(filename)
    valid_reports = 0
    valid_with_dampener = 0
    valid_with_dampener_combined = 0

    # parse input
    parsed_input = parse_input(filename)

    # pt 1
    for report in parsed_input:
        if report_safe(report):
            valid_reports += 1

    # pt 2
        if report_safe_dampener(report):
            valid_with_dampener += 1

    #pt 2 as originally intended
        if report_safe_combined(report, True):
            valid_with_dampener_combined += 1

    print(f"valid reports {version}: {valid_reports}")

    print(f"valid with dampener {version}: {valid_with_dampener}")

    print(f"valid with dampener as initially intended {version}: {valid_with_dampener_combined}")
    print("--- %s ms ---" % ((time.time_ns() - start_time) / 1000000))


main("input/day02_short.txt")
main("input/day02.txt")
