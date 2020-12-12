import sys


VECTORS = {'N': (0, -1), 'W': (-1, 0), 'S': (0, 1), 'E': (1, 0)}


def vecAdd(v, w):
    return v[0] + w[0], v[1] + w[1]


def vecMul(v, scalar):
    return v[0] * scalar, v[1] * scalar


def vecRotateLeft(v):
    return v[1], -v[0]


def vecLen(v):
    return abs(v[0]) + abs(v[1])


def navigate(instructions, course, moveFn):
    ship = (0, 0)
    for action, value in instructions:
        if action in ('N', 'E', 'S', 'W'):
            moveVec = vecMul(VECTORS[action], value)
            ship, course = moveFn(ship, course, moveVec)
        elif action == 'F':
            ship = vecAdd(ship, vecMul(course, value))
        elif action == 'L':
            for _ in range(value % 360 // 90):
                course = vecRotateLeft(course)
        elif action == 'R':
            for _ in range(value % 360 // 90):
                course = vecRotateLeft(vecRotateLeft(vecRotateLeft(course)))
    return vecLen(ship)


def partOne(instructions):
    def moveFn(ship, course, moveVec):
        return vecAdd(ship, moveVec), course
    return navigate(instructions, VECTORS['E'], moveFn)



def partTwo(instructions):
    def moveFn(ship, course, moveVec):
        return ship, vecAdd(course, moveVec)
    return navigate(instructions, (10, -1), moveFn)


if __name__ == '__main__':
    instructions = [(line[0], int(line[1:])) for line in sys.stdin]

    print("Part one:", partOne(instructions))
    print("Part two:", partTwo(instructions))
