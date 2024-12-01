
def main(filename):
    if filename.find("short") > 0:
        version = "test input"
    else:
        version = "actual input"

    # pt 1
    print(f"variable {version}: variable")
    # pt 2
    print(f"variable {version}: variable")

main("input/day0x_short.txt")
# main("input/day0x.txt")