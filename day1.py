from itertools import combinations

def partOne(expenses):
    # Nice, but slower:
    # return next(a*b for a,b in combinations(expenses, 2) if a+b == 2020)
    for i, a in enumerate(expenses):
        for b in expenses[i + 1:]:
            if a + b == 2020:
                return a * b


def partTwo(expenses):
    # Nice, but slower:
    # return next(a*b*c for a,b,c in combinations(expenses, 3) if a+b+c == 2020)
    for i, a in enumerate(expenses):
        for j, b in enumerate(expenses[i + 1:]):
            if a + b <= 2020:
                for c in expenses[j + 1:]:
                    if a + b + c == 2020:
                        return a * b * c


if __name__ == '__main__':
    with open("day1.input") as f:
        expenses = [int(x) for x in f]

    print(partOne(expenses))
    print(partTwo(expenses))
