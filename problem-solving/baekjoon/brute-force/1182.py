import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(1, n + 1):
    com = list(combinations(num, i))
    for c in com:
        if sum(c) == s:
            answer += 1

print(answer)