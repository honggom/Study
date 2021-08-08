from sys import stdin

T = int(stdin.readline())

def magic(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return magic(n-1) + magic(n-2) + magic(n-3)

for _ in range(T):
    print(magic(int(input())))