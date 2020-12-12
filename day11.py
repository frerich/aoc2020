import sys


DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def parse(f):
    for y, line in enumerate(f):
        for x, char in enumerate(line):
            if char == 'L':
                yield (x, y), False


def simulate(seats, visibleSeats, occupiedRule):
    nextSeats = dict()
    while True:
        for pos, occupied in seats.items():
            numOccupiedNeighbors = 0
            for np in visibleSeats[pos]:
                if seats[np]:
                    numOccupiedNeighbors += 1
            nextSeats[pos] = occupiedRule(occupied, numOccupiedNeighbors)

        if nextSeats == seats:
            return sum(occupied for occupied in seats.values())

        seats = nextSeats.copy()


def partOne(seats):
    def occupiedRule(currentlyOccupied, neighbors):
        return neighbors < 4 if currentlyOccupied else neighbors == 0

    visibleSeats = {}
    for x, y in seats.keys():
        visibleSeats[(x, y)] = [(x + dx, y + dy) for dx, dy in DIRECTIONS if (x + dx, y + dy) in seats]

    return simulate(seats, visibleSeats, occupiedRule)


def partTwo(seats):
    def occupiedRule(currentlyOccupied, neighbors):
        return neighbors < 5 if currentlyOccupied else neighbors == 0

    visibleSeats = {}
    for x, y in seats.keys():
        neighbors = []
        for dx, dy in DIRECTIONS:
            ax, ay = x + dx, y + dy
            while 0 <= ay < HEIGHT and 0 <= ax < WIDTH:
                if (ax, ay) in seats:
                    neighbors.append((ax, ay))
                    break
                ax += dx
                ay += dy
        visibleSeats[(x, y)] = neighbors

    return simulate(seats, visibleSeats, occupiedRule)


if __name__ == '__main__':
    WIDTH = 92
    HEIGHT = 94
    seatMap = dict(parse(sys.stdin))
    print("Part one:", partOne(seatMap))
    print("Part two:", partTwo(seatMap))
