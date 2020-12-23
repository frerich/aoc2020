import re
import sys


def parse(f):
    foodRx = re.compile(r"([a-z ]+) \(contains ([a-z, ]+)\)")
    for line in f:
        ingredients, allergens = foodRx.match(line).groups()
        yield set(ingredients.split()), set(allergens.split(", "))


def identifyAllergens():
    identifiedIngredients = set()
    potentialIngredients = {}
    allAllergens = set.union(*[allergens for _, allergens in foods])
    for allergen in allAllergens:
        potentialIngredients[allergen] = set.intersection(*[ingredients for ingredients, allergens in foods if allergen in allergens])

    while len(identifiedIngredients) < len(allAllergens):
        for allergen, candidates in potentialIngredients.items():
            candidates -= identifiedIngredients
            if len(candidates) == 1:
                ingredient = candidates.pop()
                identifiedIngredients.add(ingredient)
                yield ingredient, allergen


def partOne():
    allIngredients = set.union(*[ingredients for ingredients, _ in foods])

    result = 0
    inertIngredients = allIngredients - set(knownAllergens.keys())
    for ingredient in inertIngredients:
        result += sum(ingredient in ingredients for ingredients, _ in foods)
    return result


def partTwo():
    activeIngredients = list(knownAllergens.items())
    activeIngredients.sort(key=lambda t: t[1])
    return ",".join(ingredient for ingredient, _allergen in activeIngredients)


if __name__ == '__main__':
    foods = list(parse(sys.stdin))
    knownAllergens = dict(identifyAllergens())

    print("Part one: {}".format(partOne()))
    print("Part two: {}".format(partTwo()))
