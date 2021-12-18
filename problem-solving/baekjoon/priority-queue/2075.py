# 골드 5
# 2075. N번째 큰 수

import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    nums = list(map(int, input().split()))

    if not hq:
        for n in nums:
            heapq.heappush(hq, n)
    else:
        for n in nums:
            if hq[0] < n:
                heapq.heappop(hq)
                heapq.heappush(hq, n)

print(hq[0])