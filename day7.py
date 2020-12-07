from collections import defaultdict
import re
import sys


def parse(line):
    container, contained = line.rstrip()[:-1].split(" bags contain ")

    bags = {}
    for item in contained.split(", "):
        match = re.match(r"(\d+) ([a-z ]+) bags?", item)
        if match is not None:
            bags[match.group(2)] = int(match.group(1))

    return (container, bags)


def containingBags(table, color):
    children = table[color]
    return children.union(*[containingBags(table, c) for c in children])


def numContainedBags(table, color):
    result = 0
    for containedColor, count in table[color].items():
        result += count * (1 + numContainedBags(table, containedColor))
    return result


def partOne(table):
    reverseTable = defaultdict(set)
    for container, bags in table.items():
        for color, _ in bags.items():
            reverseTable[color].add(container)

    return len(containingBags(reverseTable, "shiny gold"))


def partTwo(table):
    return numContainedBags(table, "shiny gold")


if __name__ == '__main__':
    containers = dict(parse(line) for line in sys.stdin)
    print("Part one:", partOne(containers))
    print("Part two:", partTwo(containers))
