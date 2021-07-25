from sys import stdin

while True:
    a, b = map(int, stdin.readline().split())
    if a == 0 and b == 0:
        break
    elif b > a and b / a == int(b / a) and int(b / a) > 0:
        print("factor")
    elif a > b and a / b == int(a / b) and int(a / b) > 0:
        print("multiple")
    else:
        print("neither")
