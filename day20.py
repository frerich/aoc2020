from math import sqrt
import sys


SEAMONSTER_TEMPLATE = """\
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
TILE_SIZE = 10


def parse(f):
    blocks = f.read().rstrip().split('\n\n')

    for block in blocks:
        lines = block.split('\n')

        tileId = int(lines[0][5:-1])
        pixels = set()
        for y, line in enumerate(lines[1:]):
            for x, ch in enumerate(line):
                if ch == '#':
                    pixels.add((x, y))

        yield tileId, pixels


def rotateLeft(tile, width=TILE_SIZE):
    return {(y, -x + width - 1) for x, y in tile}


def mirrorVertical(tile, height=TILE_SIZE):
    return {(x, height - 1 - y) for x, y in tile}


def imageVariants(tile, size=TILE_SIZE):
    result = []

    result.append(mirrorVertical(tile, size))
    result.append(rotateLeft(result[-1], size))
    result.append(rotateLeft(result[-1], size))
    result.append(rotateLeft(result[-1], size))

    result.append(tile)
    result.append(rotateLeft(result[-1], size))
    result.append(rotateLeft(result[-1], size))
    result.append(rotateLeft(result[-1], size))

    return result


def verticalBorderMatches(leftTile, rightTile):
    return all(((TILE_SIZE - 1, y) in leftTile) == ((0, y) in rightTile) for y in range(TILE_SIZE))


def horizontalBorderMatches(topTile, bottomTile):
    return all(((x, TILE_SIZE - 1) in topTile) == ((x, 0) in bottomTile) for x in range(TILE_SIZE))


def arrange(image):
    if len(image) == len(tiles):
        return image

    leftTile, aboveTile = None, None
    if image:
        if len(image) % imageWidth > 0:
            leftTile = image[-1][1]
        if len(image) // imageWidth > 0:
            aboveTile = image[-imageWidth][1]

    usedTiles = set(tileId for tileId, _ in image)

    for tileId, variants in tiles.items():
        if tileId in usedTiles:
            continue

        for variant in variants:
            if leftTile and not verticalBorderMatches(leftTile, variant):
                continue

            if aboveTile and not horizontalBorderMatches(aboveTile, variant):
                continue

            result = arrange(image + [(tileId, variant)])
            if result:
                return result

    return None


def partOne():
    return arrangement[0][0] * arrangement[imageWidth - 1][0] * arrangement[-imageWidth][0] * arrangement[-1][0]


def partTwo():
    border = set()
    border.update({(x, 0) for x in range(TILE_SIZE)})
    border.update({(x, TILE_SIZE - 1) for x in range(TILE_SIZE)})
    border.update({(0, y) for y in range(TILE_SIZE)})
    border.update({(TILE_SIZE - 1, y) for y in range(TILE_SIZE)})

    composedImage = set()
    for pos, (_, tile) in enumerate(arrangement):
        xOffset = (pos % imageWidth) * (TILE_SIZE - 2)
        yOffset = (pos // imageWidth) * (TILE_SIZE - 2)
        transposedTile = {(x + xOffset - 1, y + yOffset - 1) for x, y in tile - border}
        composedImage.update(transposedTile)

    seaMonsterTemplate = set()
    for y, line in enumerate(SEAMONSTER_TEMPLATE.split('\n')):
        for x, ch in enumerate(line):
            if ch == '#':
                seaMonsterTemplate.add((x, y))

    imageWidthPx = imageWidth * (TILE_SIZE - 2)

    for variant in imageVariants(composedImage, imageWidthPx):
        seaMonsterPixels = set()
        for y in range(imageWidthPx):
            for x in range(imageWidthPx):
                seaMonster = {(a + x, b + y) for a, b in seaMonsterTemplate}
                if seaMonster.issubset(variant):
                    seaMonsterPixels.update(seaMonster)

        if seaMonsterPixels:
            return len(variant - seaMonsterPixels)


if __name__ == '__main__':
    tiles = {tileId: imageVariants(tile) for tileId, tile in parse(sys.stdin)}
    imageWidth = int(sqrt(len(tiles)))
    arrangement = arrange([])
    print("Part one: {}".format(partOne()))
    print("Part two: {}".format(partTwo()))
