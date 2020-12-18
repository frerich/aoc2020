import sys


def evalProduct(tokens, i):
    lhs, i = evalSum(tokens, i)
    if tokens[i] != '*':
        return lhs, i
    rhs, i = evalProduct(tokens, i + 1)
    return lhs * rhs, i


def evalSum(tokens, i):
    lhs, i = evalSummand(tokens, i)
    if tokens[i] != '+':
        return lhs, i
    rhs, i = evalSum(tokens, i + 1)
    return lhs + rhs, i


def evalSummand(tokens, i):
    if tokens[i] == '(':
        value, i = evalProduct(tokens, i + 1)
    else:
        value = int(tokens[i])
    return value, i + 1


def evalOperand(tokens, i):
    if tokens[i] == '(':
        result, i = evalPart1(tokens, i + 1)
    else:
        result = int(tokens[i])
    return result, i + 1


def evalPart1(tokens, i=0):
    result, i = evalOperand(tokens, i)

    while tokens[i] != ')':
        operator = tokens[i]
        i += 1

        operand, i = evalOperand(tokens, i)
        if operator == '+':
            result += operand
        else:
            result *= operand

    return result, i


def tokenize(line):
    return line.replace("(", "( ").replace(")", " )").split() + [')']


if __name__ == '__main__':
    lines = list(sys.stdin)
    print("Part one:", sum(evalPart1(tokenize(line), 0)[0] for line in lines))
    print("Part two:", sum(evalProduct(tokenize(line), 0)[0] for line in lines))
