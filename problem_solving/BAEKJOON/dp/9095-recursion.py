from sys import stdin

t = int(stdin.readline())


def get_card_cases(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return get_card_cases(n-1) + get_card_cases(n-2) + get_card_cases(n-3)


for _ in range(t):
    print(get_card_cases(int(input())))