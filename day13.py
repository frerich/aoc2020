import sys


def parse(f):
    departure = int(f.readline())
    tokens = f.readline().split(",")
    busses = [(busIdx, int(bus)) for busIdx, bus in enumerate(tokens) if bus != 'x']
    return departure, busses


def partOne(departure, busses):
    waitingTime, bus = min([(bus - departure % bus, bus) for _, bus in busses])
    return waitingTime * bus


def partTwo(departure, busses):
    _, period = busses[0]
    t = 0
    for busIdx, bus in busses[1:]:
        offset = None
        while True:
            if (t + busIdx) % bus == 0:
                if offset is None:
                    offset = t
                else:
                    period = t - offset
                    break

            t += period

    return offset


if __name__ == '__main__':
    departure, busses = parse(sys.stdin)

    print("Part one:", partOne(departure, busses))
    print("Part two:", partTwo(departure, busses))
