import sys


def partOne(instructions):
    memory = {}

    for instr in instructions:
        lhs, _, rhs = instr.split()
        if lhs.startswith('mask'):
            fixedValue = int(''.join('0' if c == 'X' else c for c in rhs), 2)
            mask = int(''.join('1' if c == 'X' else '0' for c in rhs), 2)
        elif lhs.startswith('mem'):
            addr = int(lhs[lhs.find('[') + 1:-1])
            value = int(rhs)
            memory[addr] = fixedValue | (value & mask)

    return sum(memory.values())


def partTwo(instructions):
    memory = {}

    for instr in instructions:
        lhs, _, rhs = instr.split()
        if lhs.startswith('mask'):
            mask = int(''.join('1' if c == '1' else '0' for c in rhs), 2)
            floatMask = int(''.join('0' if c == 'X' else '1' for c in rhs), 2)

            addrVariantMasks = []
            floatBits = [pos for pos, c in enumerate(reversed(rhs)) if c == 'X']
            for variant in range(2 ** len(floatBits)):
                variantMask = 0
                for n, pos in enumerate(floatBits):
                    variantMask |= ((variant >> n) & 1) << pos
                addrVariantMasks.append(variantMask)

        elif lhs.startswith('mem'):
            addr = int(lhs[lhs.find('[') + 1:-1])
            value = int(rhs)

            addr |= mask

            for variantMask in addrVariantMasks:
                memory[(addr & floatMask) | variantMask] = value

    return sum(memory.values())


if __name__ == '__main__':
    lines = list(sys.stdin)
    print("Part one:", partOne(lines))
    print("Part two:", partTwo(lines))
