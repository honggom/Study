# 실버 2
# 1541. 잃어버린 괄호

import sys
input = sys.stdin.readline

s = input().rstrip().split('-')
nums = []

for c in s:
    plus = c.split('+')
    _sum = 0

    for p in plus:
        _sum += int(p)
    nums.append(_sum)

n = nums[0]

for i in range(1, len(nums)):
    n -= nums[i]

print(n)