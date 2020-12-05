def parse(code):
    digits = ['1' if c in ('B', 'R') else '0' for c in code]
    return int(''.join(digits), 2)


def partOne(ids):
    return max(ids)


def partTwo(ids):
    for x in ids:
        if x + 1 not in ids and x + 2 in ids:
            return x + 1


if __name__ == '__main__':
    with open("day5.input") as f:
        seatIds = set(parse(line.rstrip()) for line in f)

    print("Part one:", partOne(seatIds))
    print("Part two:", partTwo(seatIds))
