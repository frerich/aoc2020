import sys


def parse(group):
    return [set(answers) for answers in group.split('\n')]


if __name__ == '__main__':
    groups = [parse(group) for group in sys.stdin.read().rstrip().split('\n\n')]

    print("Part one:", sum(len(set.union(*g)) for g in groups))
    print("Part two:", sum(len(set.intersection(*g)) for g in groups))
