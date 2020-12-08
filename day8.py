import sys


class Machine:
    def __init__(self, program):
        self.program = program
        self.ip = 0
        self.acc = 0

    def step(self):
        cmd, arg = self.program[self.ip]
        self.ip += 1
        if cmd == 'nop':
            pass
        elif cmd == 'jmp':
            self.ip += arg - 1
        elif cmd == 'acc':
            self.acc += arg

    def done(self):
        return not 0 <= self.ip < len(self.program)


def runUntilLoop(machine):
    seen = set()
    while not machine.done() and machine.ip not in seen:
        seen.add(machine.ip)
        machine.step()


def partOne(program):
    m = Machine(program)
    runUntilLoop(m)
    return m.acc


def partTwo(program):
    for i, (cmd, arg) in enumerate(program):
        if cmd == 'nop':
            program[i] = ('jmp', arg)
        elif cmd == 'jmp':
            program[i] = ('nop', arg)
        else:
            continue

        m = Machine(program)
        runUntilLoop(m)
        if m.done():
            return m.acc

        program[i] = (cmd, arg)


def parse(line):
    cmd, arg = line.split()
    return cmd, int(arg)


if __name__ == '__main__':
    program = [parse(line) for line in sys.stdin]

    print("Part one:", partOne(program))
    print("Part two:", partTwo(program))
