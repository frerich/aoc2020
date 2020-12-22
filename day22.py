import sys


def score(deck):
    multiplicators = range(len(deck), 0, -1)
    return sum(card * factor for card, factor in zip(deck, multiplicators))


def combat(deckA, deckB):
    while deckA and deckB:
        cardA, cardB = deckA.pop(0), deckB.pop(0)
        if cardA > cardB:
            deckA += [cardA, cardB]
        else:
            deckB += [cardB, cardA]

    return deckA, deckB


def recursiveCombat(deckA, deckB):
    seen = set()
    while deckA and deckB:
        tupleA, tupleB = tuple(deckA), tuple(deckB)
        if (tupleA, tupleB) in seen:
            return deckA, []
        seen.add((tupleA, tupleB))

        cardA, cardB = deckA.pop(0), deckB.pop(0)

        if len(deckA) >= cardA and len(deckB) >= cardB:
            subDeckA, subDeckB = recursiveCombat(deckA[:cardA], deckB[:cardB])
            player1Wins = len(subDeckA) > 0
        else:
            player1Wins = cardA > cardB

        if player1Wins:
            deckA += [cardA, cardB]
        else:
            deckB += [cardB, cardA]

    return deckA, deckB


def parse(f):
    blocks = f.read().rstrip().split('\n\n')

    decks = []
    for block in blocks:
        decks.append([int(line) for line in block.split('\n')[1:]])
    return decks


def play(game, deckA, deckB):
    finalDeckA, finalDeckB = game(deckA.copy(), deckB.copy())
    winningDeck = finalDeckA if finalDeckA else finalDeckB
    return score(winningDeck)


if __name__ == '__main__':
    deckA, deckB = parse(sys.stdin)

    print("Part one:", play(combat, deckA, deckB))
    print("Part two:", play(recursiveCombat, deckA, deckB))
