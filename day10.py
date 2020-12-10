import sys


OUTLET_JOLTAGE = 0


def partOne(joltages):
    deltas = [b - a for a, b in zip(joltages, joltages[1:])]
    return deltas.count(1) * deltas.count(3)


def partTwo(joltages):
    compatible = {}
    for i, joltage in enumerate(joltages[:-1]):
        compatible[joltage] = [j for j in joltages[i+1:i+4] if j - joltage <= 3]

    numArrangements = {joltages[-1]: 1}
    for joltage in reversed(joltages[:-1]):
        numArrangements[joltage] = sum(numArrangements[j] for j in compatible[joltage])

    return numArrangements[OUTLET_JOLTAGE]


if __name__ == '__main__':
    adapters = sorted(int(line) for line in sys.stdin)
    joltages = [OUTLET_JOLTAGE] + adapters + [adapters[-1] + 3]

    print("Part one:", partOne(joltages))
    print("Part two:", partTwo(joltages))
