DOOR_PUBKEY = 14205034
CARD_PUBKEY = 18047856


def transformSubjectNumber(subject):
    value = 1
    while True:
        yield value
        value = (value * subject) % 20201227


def partOne():
    for cardLoopSize, pubKey in enumerate(transformSubjectNumber(7)):
        if pubKey == CARD_PUBKEY:
            break

    for loopNo, encryptionKey in enumerate(transformSubjectNumber(DOOR_PUBKEY)):
        if loopNo == cardLoopSize:
            return encryptionKey


if __name__ == '__main__':
    print("Part one:", partOne())
