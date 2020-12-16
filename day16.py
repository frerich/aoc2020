from collections import defaultdict
import re
import sys


def parse(f):
    data = f.read().rstrip()
    blocks = data.split('\n\n')

    fieldRules = {}
    ruleRx = r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)"
    for line in blocks[0].split('\n'):
        field, minA, maxA, minB, maxB = re.match(ruleRx, line).groups()
        fieldRules[field] = ((int(minA), int(maxA)), (int(minB), int(maxB)))

    myTicket = [int(value) for value in blocks[1].split('\n')[1].split(',')]

    nearbyTickets = []
    for ticket in blocks[2].split('\n')[1:]:
        nearbyTickets.append([int(value) for value in ticket.split(',')])

    return fieldRules, myTicket, nearbyTickets


def boundsMatch(bounds, value):
    (minA, maxA), (minB, maxB) = bounds
    return minA <= value <= maxA or minB <= value <= maxB


def partOne(rules, tickets):
    ticketScanningErrorRate = 0
    for ticket in tickets:
        for value in ticket:
            valid = any(boundsMatch(bounds, value) for bounds in rules.values())
            if not valid:
                ticketScanningErrorRate += value
    return ticketScanningErrorRate


def partTwo(rules, myTicket, tickets):
    allTickets = tickets + [myTicket]

    validTickets = []
    for ticket in allTickets:
        validTicket = True
        for value in ticket:
            if not any(boundsMatch(bounds, value) for bounds in rules.values()):
                validTicket = False
                break

        if validTicket:
            validTickets.append(ticket)

    fieldCandidates = defaultdict(list)
    for fieldIdx, values in enumerate(zip(*validTickets)):
        for name, bounds in rules.items():
            if all(boundsMatch(bounds, value) for value in values):
                fieldCandidates[name].append(fieldIdx)

    fieldMap = {}
    while fieldCandidates:
        name, [fieldIdx] = next(x for x in fieldCandidates.items() if len(x[1]) == 1)
        del fieldCandidates[name]
        fieldMap[name] = fieldIdx
        for candidates in fieldCandidates.values():
            candidates.remove(fieldIdx)

    result = 1
    for name, idx in fieldMap.items():
        if name.startswith("departure"):
            result *= myTicket[idx]

    return result


if __name__ == '__main__':
    fieldRules, myTicket, nearbyTickets = parse(sys.stdin)
    print("Part one:", partOne(fieldRules, nearbyTickets))
    print("Part two:", partTwo(fieldRules, myTicket, nearbyTickets))
