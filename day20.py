from math import sqrt
import sys


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


def rotateLeft(pixels):
    return {(y, -x + TILE_SIZE - 1) for x, y in pixels}


def mirrorVertical(pixels):
    return {(x, TILE_SIZE - 1 - y) for x, y in pixels}


def mirrorHorizontal(pixels):
    return {(TILE_SIZE - 1 - x, y) for x, y in pixels}


def variants(pixels):
    result = [pixels]
    result.append(rotateLeft(result[-1]))
    result.append(rotateLeft(result[-1]))
    result.append(rotateLeft(result[-1]))

    result.append(mirrorVertical(pixels))
    result.append(rotateLeft(result[-1]))
    result.append(rotateLeft(result[-1]))
    result.append(rotateLeft(result[-1]))

    result.append(mirrorHorizontal(pixels))
    result.append(rotateLeft(result[-1]))
    result.append(rotateLeft(result[-1]))
    result.append(rotateLeft(result[-1]))

    return result


def render(tile):
    for y in range(TILE_SIZE):
        for x in range(TILE_SIZE):
            sys.stdout.write('#' if (x, y) in tile else '.')
        sys.stdout.write('\n')


if __name__ == '__main__':
    upper_edge = {(x, 0) for x in range(TILE_SIZE)}
    variantEdges = {}
    for tileId, pixels in parse(sys.stdin):
        edges = []
        for variant in [pixels, mirrorVertical(pixels), mirrorHorizontal(pixels)]:
            es = []
            for _ in range(4):
                es.append(variant & upper_edge)
                variant = rotateLeft(variant)
            edges.append(es)
        variantEdges[tileId] = edges

    for tileId, variants in variantEdges.items():
        for otherTileId, otherVariants in variantEdges.items():
            if otherTileId == tileId:
                continue

            for variant in variants:
                if variant[0] in 

            if variant[0] in
