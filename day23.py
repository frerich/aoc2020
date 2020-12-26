PUZZLE_INPUT = "364297581"
EXAMPLE_INPUT = "389125467"


def move(currentCup, succ):
    p0 = succ[currentCup]
    p1 = succ[p0]
    p2 = succ[p1]
    nextCup = succ[p2]

    destCup = currentCup - 1
    while True:
        if destCup < 1:
            destCup = max(succ)
        if destCup not in (p0, p1, p2):
            break
        destCup = destCup - 1

    succ[currentCup] = nextCup
    succ[p2] = succ[destCup]
    succ[destCup] = p0
    return nextCup


def partOne(puzzleInput):
    currentCup, successors = parse(puzzleInput)
    for _ in range(100):
        currentCup = move(currentCup, successors)

    cups = []
    cup = successors[1]
    while cup != 1:
        cups.append(str(cup))
        cup = successors[cup]
    return ''.join(cups)


def partTwo(puzzleInput):
    currentCup, successors = parse(puzzleInput)
    ms = max(successors)
    successors.extend(range(ms + 2, 1000000 + 2))
    successors[int(puzzleInput[-1])] = ms + 1
    successors[1000000] = int(puzzleInput[0])

    for _ in range(10000000):
        currentCup = move(currentCup, successors)

    return successors[1] * successors[successors[1]]


def parse(puzzleInput):
    startCup = int(puzzleInput[0])
    successors = [0] * (len(puzzleInput) + 1)

    for i in range(len(puzzleInput) - 1):
        successors[int(puzzleInput[i])] = int(puzzleInput[i + 1])
    successors[int(puzzleInput[-1])] = startCup

    return startCup, successors


if __name__ == '__main__':
    print("Part one: {}".format(partOne(PUZZLE_INPUT)))
    print("Part two: {}".format(partTwo(PUZZLE_INPUT)))
