# 실버 4
# 2847. 게임을 만든 동준이

import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(int(input()))]
count = 0

for i in range(len(nums) - 1, 0, -1):
    if nums[i - 1] >= nums[i]:
        count += nums[i - 1] - (nums[i] - 1)
        nums[i - 1] = nums[i] - 1

print(count)