import heapq
import sys
input = sys.stdin.readline

t = int(input())
hq = []

for _ in range(t):
    n = int(input())

    if n == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, [abs(n), n])
