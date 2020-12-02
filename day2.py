import re

def parse(line):
    lo, hi, char, password = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line).groups()
    return int(lo), int(hi), char, password

def validRentalSledPassword(lo, hi, char, password):
    return lo <= password.count(char) <= hi

def validOTCAPassword(i, j, char, password):
    return (password[i - 1] == char) != (password[j - 1] == char)

if __name__ == '__main__':
    with open("day2.input") as f:
        passwords = [parse(line) for line in f]

    print("Part one:", sum(validRentalSledPassword(*pw) for pw in passwords))
    print("Part two:", sum(validOTCAPassword(*pw) for pw in passwords))
