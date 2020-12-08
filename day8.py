import sys


def parse(line):
    cmd, arg = line.split()
    return cmd, int(arg)


def execute(program):
    ip, acc = 0, 0
    visited = set()
    while ip < len(program):
        if ip in visited:
            return True, acc
        visited.add(ip)

        cmd, arg = program[ip]

        if cmd == 'nop':
            ip, acc = ip + 1, acc
        elif cmd == 'jmp':
            ip, acc = ip + arg, acc
        elif cmd == 'acc':
            ip, acc = ip + 1, acc + arg

    return False, acc


def partOne(program):
    loops, acc = execute(program)
    return acc


def partTwo(program):
    for i, (cmd, arg) in enumerate(program):
        if cmd == 'nop':
            patched = program.copy()
            patched[i] = ('jmp', arg)
        elif cmd == 'jmp':
            patched = program.copy()
            patched[i] = ('nop', arg)
        else:
            continue

        loops, acc = execute(patched)
        if not loops:
            return acc


if __name__ == '__main__':
    program = [parse(line) for line in sys.stdin]

    print("Part one:", partOne(program))
    print("Part two:", partTwo(program))
