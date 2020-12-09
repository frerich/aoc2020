from itertools import combinations
import sys


def partOne(numbers, preambleLen):
    for i, n in enumerate(numbers[preambleLen:], start=preambleLen):
        sums = set(sum(pair) for pair in combinations(numbers[i-preambleLen:i], 2))
        if n not in sums:
            return n
    return None


def partTwo(numbers, targetSum):
    runSums = numbers.copy()
    for runLength in range(2, len(numbers)):
        runSums.pop()
        for i in range(len(runSums)):
            runSums[i] += numbers[i + runLength - 1]
            if runSums[i] == targetSum:
                run = numbers[i:i + runLength]
                return min(run) + max(run)


if __name__ == '__main__':
    numbers = [int(line) for line in sys.stdin]

    firstAnswer = partOne(numbers, 25)
    print("Part one:", firstAnswer)
    print("Part two:", partTwo(numbers, firstAnswer))
