from itertools import product
import sys


def parse(f):
    for y, line in enumerate(f):
        for x, ch in enumerate(line):
            if ch == '#':
                yield x, y


def evolve(active, dimensions):
    bounds = []
    for dim in range(dimensions):
        cs = [v[dim] for v in active]
        bounds.append((min(cs), max(cs)))

    space = product(*[range(bounds[dim][0] - 1, bounds[dim][1] + 2) for dim in range(dimensions)])

    for v in space:
        # Hot path: don't use `sum` or generator expressions here
        activeNeighbors = 0
        for va in product(*[[c - 1, c, c + 1] for c in v]):
            if va != v and va in active:
                activeNeighbors += 1

        if v in active and activeNeighbors in (2, 3) or v not in active and activeNeighbors == 3:
            yield v


def simulate(active, dimensions, rounds):
    for _ in range(rounds):
        active = set(evolve(active, dimensions))
    return len(active)


if __name__ == '__main__':
    initialSlice = set(parse(sys.stdin))

    print("Part one:", simulate(set((x, y, 0) for x, y in initialSlice), 3, 6))
    print("Part one:", simulate(set((x, y, 0, 0) for x, y in initialSlice), 4, 6))
