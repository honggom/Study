# 실버 5
# 4796. 캠핑

import sys
input = sys.stdin.readline

count = 1
while True:
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    a = l if v % p > l else v % p
    b = (v // p) * l

    print(f'Case {count}: {a + b}')
    count += 1