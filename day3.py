def parse(fn):
    with open(fn) as f:
        lines = [line.rstrip() for line in f]
        width = len(lines[0])
        height = len(lines)
        trees = set()

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char == '#':
                    trees.add((x, y))

        return width, height, trees


def slide(trees, width, height, dx, dy):
    x, y = 0, 0
    while y < height:
        if (x,y) in trees:
            yield x, y
        x = (x + dx) % width
        y += dy


def partOne(width, height, trees):
    return sum(1 for _ in slide(trees, width, height, 3, 1))


def partTwo(width, height, trees):
    result = 1
    for dx, dy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
        result *= sum(1 for _ in slide(trees, width, height, dx, dy))
    return result


if __name__ == '__main__':
    width, height, trees = parse("day3.input")
    print("Part one:", partOne(width, height, trees))
    print("Part two:", partTwo(width, height, trees))
