# 실버 4
# 2960. 에라토스테네스의 체

import sys

n, k = map(int, input().split())
nums = [i for i in range(2, n + 1)]
count = 0
temp = []

while nums:
    pivot = nums[0]

    for i in range(len(nums)):
        if nums[i] / pivot == int(nums[i] / pivot):
            temp.append(nums[i])

    for j in temp:
        nums.remove(j)
        count += 1
        if count == k:
            print(j)
            sys.exit(0)

    temp.clear()