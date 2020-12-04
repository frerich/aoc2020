def parse(data):
    return dict(field.split(':') for field in data.split())


def passportComplete(passport):
    return all(f in passport for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def passportValid(passport):
    return passportComplete(passport) and all(fieldValid(*field) for field in passport.items())


def fieldValid(name, value):
    if name == 'byr':
        return len(value) == 4 and value.isdigit() and 1920 <= int(value) <= 2002

    if name == 'iyr':
        return len(value) == 4 and value.isdigit() and 2010 <= int(value) <= 2020

    if name == 'eyr':
        return len(value) == 4 and value.isdigit() and 2020 <= int(value) <= 2030

    if name == 'hgt':
        if value.endswith('cm'):
            number = value[:-2]
            return number.isdigit() and 150 <= int(number) <= 193

        if value.endswith('in'):
            number = value[:-2]
            return number.isdigit() and 59 <= int(number) <= 76

        return False

    if name == 'hcl':
        return len(value) == 7 \
           and value[0] == '#' \
           and all(c in "0123456789abcdef" for c in value[1:])

    if name == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if name == 'pid':
        return len(value) == 9 and value.isdigit()

    if name == 'cid':
        pass # Ignored

    return True


if __name__ == '__main__':
    with open("day4.input") as f:
        passports = [parse(fields) for fields in f.read().split('\n\n')]

    print("Part one:", sum(passportComplete(p) for p in passports))
    print("Part two:", sum(passportValid(p) for p in passports))
