PUZZLE_INPUT = [6,4,12,1,20,0,16]


def sequence(startingNumbers):
    spokenNumbers = {x: i for i, x in enumerate(startingNumbers)}
    yield from spokenNumbers.keys()

    nextNumber = 0
    turn = len(startingNumbers)
    while True:
        yield nextNumber

        lastOcc = spokenNumbers.get(nextNumber, turn)
        spokenNumbers[nextNumber] = turn

        nextNumber = turn - lastOcc
        turn += 1


def nth(iterable, n):
    for _ in range(n - 1):
        next(iterable)
    return next(iterable)


if __name__ == '__main__':
    print("Part one:", nth(sequence(PUZZLE_INPUT), 2020))
    print("Part two:", nth(sequence(PUZZLE_INPUT), 30000000))
