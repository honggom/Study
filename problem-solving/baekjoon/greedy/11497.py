# 실버 1
# 11497. 통나무 건너뛰기

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    left, right = deque(), deque()
    n = int(input())
    nums = sorted(list(map(int, input().split())))

    for i in range(len(nums)):
        if i % 2 == 0:
            left.append(nums[i])
        else:
            right.appendleft(nums[i])

    result = 0
    srted = left + right

    for i in range(len(srted) - 1):
        result = max(result, abs(srted[i] - srted[i + 1]))
    result = max(result, abs(srted[0] - srted[-1]))

    print(result)