import sys
input = sys.stdin.readline

n = int(input())
l = sorted(sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0]), key=lambda x: x[1])

count = 0
last = 0
for a, b in l:
    if last <= a:
        count += 1
        last = b
print(count)