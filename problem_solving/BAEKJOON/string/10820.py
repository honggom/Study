import sys

while True:
    result = [0, 0, 0, 0]
    string = sys.stdin.readline().rstrip('\n')

    if not string:
        break
    for s in string:
        if s.islower():
            result[0] += 1
        elif s.isupper():
            result[1] += 1
        elif s.isnumeric():
            result[2] += 1
        elif s == " ":
            result[3] += 1

    print(*result)
