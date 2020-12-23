INPUT = [int(x) for x in "364297581"]


def move(cups):
    currentCup = cups.pop(0)
    destCup = currentCup - 1
    while True:
        if destCup < 1:
            destCup = max(cups)
        if destCup not in cups[:3]:
            break
        destCup -= 1

    destIdx = cups.index(destCup)
    return cups[3:destIdx + 1] + cups[:3] + cups[destIdx + 1:] + [currentCup]


def partOne():
    cups = INPUT.copy()
    for _ in range(100):
        cups = move(cups)
    result = cups[cups.index(1) + 1:] + cups[:cups.index(1)]
    return ''.join(str(label) for label in result)


if __name__ == '__main__':
    print("Part one: {}".format(partOne()))
