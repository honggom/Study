# 골드 2
# 2696. 중앙값 구하기

import heapq
import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = []
    for _ in range(math.ceil(n / 10)):
        nums = nums + list(map(int, input().split()))

    count = 0
    result = []
    max_heap = []
    min_heap = []

    for i in range(len(nums)):

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, -nums[i])
        else:
            heapq.heappush(min_heap, nums[i])

        if len(max_heap) > 0 and len(min_heap) > 0 and max_heap[0] * -1 > min_heap[0]:
            max_value = heapq.heappop(max_heap) * -1
            min_value = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -min_value)
            heapq.heappush(min_heap, max_value)

        if (i + 1) % 2 != 0:
            count += 1
            result.append(max_heap[0] * -1)

    print(count)
    new_line_count = 0
    for j in range(len(result)):
        new_line_count += 1
        if new_line_count == 10:
            print(result[j])
            new_line_count = 0
        elif j == len(result) - 1:
            print(result[j])
        else:
            print(result[j], end=" ")