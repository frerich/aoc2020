import re

def parse(line):
    min, max, char, password = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line).groups()
    return int(min), int(max), char, password

def validRentalSledPassword(min, max, char, password):
    return min <= password.count(char) <= max

def validOTCAPassword(i, j, char, password):
    return (password[i - 1] == char) != (password[j - 1] == char)

if __name__ == '__main__':
    with open("day2.input") as f:
        passwords = [parse(line) for line in f]

    print("Part one:", sum(1 for pw in passwords if validRentalSledPassword(*pw)))
    print("Part one:", sum(1 for pw in passwords if validOTCAPassword(*pw)))
