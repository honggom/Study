import sys
input = sys.stdin.readline

count = 1
while True:
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    result = (v % p) + ((v // p) * l)

    print(f'Case {count}: {result}')
    count += 1