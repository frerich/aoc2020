from functools import cache
import sys


def parse(f):
    data = f.read().rstrip()
    blocks = data.split('\n\n')

    productions = {}
    terminals = {}
    for line in blocks[0].split('\n'):
        ruleNo, alternatives = line.split(': ')
        if alternatives.startswith('"'):
            terminals[int(ruleNo)] = alternatives[1:-1]
        else:
            productions[int(ruleNo)] = []
            for alternative in alternatives.split(' | '):
                productions[int(ruleNo)].append([int(n) for n in alternative.split()])

    receivedMessages = blocks[1].split('\n')
    return productions, terminals, set(receivedMessages)


@cache
def possibleMessages(ruleNo):
    if ruleNo in terminals:
        return set(terminals[ruleNo])

    result = set()
    for alternative in productions[ruleNo]:
        result.update(expandAlternative(alternative))
    return result


def expandAlternative(rules):
    if len(rules) == 1:
        return possibleMessages(rules[0])

    result = set()
    for prefix in possibleMessages(rules[0]):
        for suffix in expandAlternative(rules[1:]):
            result.add(prefix + suffix)
    return result


def partOne():
    prefixes = tuple(possibleMessages(42))
    suffixes = tuple(possibleMessages(31))

    assert all(len(x) == len(prefixes[0]) for x in prefixes)
    assert all(len(x) == len(suffixes[0]) for x in suffixes)

    prefix_len = len(prefixes[0])

    numValidMessages = 0
    for msg in receivedMessages:
        rule8_matches = msg[:prefix_len] in prefixes
        rule11_matches = msg[prefix_len:2*prefix_len] in prefixes and msg[2*prefix_len:] in suffixes
        if rule8_matches and rule11_matches:
            numValidMessages += 1
    return numValidMessages


def partTwo():
    numValidMessages = 0

    prefixes = tuple(possibleMessages(42))
    suffixes = tuple(possibleMessages(31))

    assert all(len(x) == len(prefixes[0]) for x in prefixes)
    assert all(len(x) == len(suffixes[0]) for x in suffixes)

    prefix_len = len(prefixes[0])
    suffix_len = len(suffixes[0])

    for msg in receivedMessages:
        # Reverse rule 11 at least once
        rule11_matched = False
        while msg.startswith(prefixes) and msg.endswith(suffixes):
            msg = msg[prefix_len:-suffix_len]
            rule11_matched = True
        if not rule11_matched:
            continue

        # Reverse rule 8 at least once
        rule8_matched = False
        while msg.startswith(prefixes):
            msg = msg[prefix_len:]
            rule8_matched = True
        if not rule8_matched:
            continue

        if not msg:
            numValidMessages += 1

    return numValidMessages


if __name__ == '__main__':
    productions, terminals, receivedMessages = parse(sys.stdin)
    print("Part one:", partOne())
    print("Part two:", partTwo())
