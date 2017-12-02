import itertools

def part1():
    checksum = 0
    for l in open('input.txt'):
        line = l.replace('\n', '')
        low = 10000
        high = 0

        row = [int(x) for x in line.split('\t')]

        row.sort()
        low = min(row)
        high = max(row)

        checksum += (high - low)

    print(f"checksum: {checksum}")

def part2():
    result = 0
    for l in open('input.txt'):
        line = l.replace('\n', '')
        row = [int(x) for x in line.split('\t')]

        def is_even(a, b):
            c, d = a / b, b / a

            return c == int(c) or d == int(d)

        for x in itertools.combinations(row, 2):
            a = x[0]
            b = x[1]
            if is_even(*x):
                if a % b == 0: result += (a / b)
                elif b % a == 0: result += (b / a)

    print(f"result: {result}")

part1()
part2()
