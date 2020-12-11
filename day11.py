import sys


DIRECTIONS = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]


def parse(f):
    for y, line in enumerate(f):
        for x, char in enumerate(line):
            if char == 'L':
                yield (x, y), False


def evolve(seats):
    for (x, y), occupied in seats.items():
        neighbors = sum(seats.get((x+dx, y+dy), False) for dx, dy in DIRECTIONS)

        if occupied:
            stillOccupied = neighbors < 4
        else:
            stillOccupied = neighbors == 0

        yield (x, y), stillOccupied


def evolve2(seats):
    for (x, y), occupied in seats.items():
        neighbors = 0

        for dx, dy in DIRECTIONS:
            px, py = x + dx, y + dy
            while 0 <= px < 92 and 0 <= py < 94:
                seatTaken = seats.get((px, py))
                if seatTaken is not None:
                    neighbors += seatTaken
                    break
                px += dx
                py += dy

        if occupied:
            stillOccupied = neighbors < 5
        else:
            stillOccupied = neighbors == 0

        yield (x, y), stillOccupied


def simulate(seats, evolveFn):
    prevSeats = seats
    while True:
        prevSeats, seats = seats, dict(evolveFn(seats))
        if seats == prevSeats:
            return sum(occupied for occupied in seats.values())


if __name__ == '__main__':
    seats = dict(parse(sys.stdin))

    print("Part one:", simulate(seats, evolve))
    print("Part two:", simulate(seats, evolve2))
