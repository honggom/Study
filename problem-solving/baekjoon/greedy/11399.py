import sys
input = sys.stdin.readline

n = int(input())
ns = sorted(list(map(int, input().split())))
count = 0

if n == 1:
    print(ns[0])
else:
    for i in range(1, len(ns)):
        ns[i] += ns[i - 1]
    print(sum(ns))
