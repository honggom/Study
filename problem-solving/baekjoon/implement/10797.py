from collections import Counter

n = int(input())
nums = Counter(list(map(int, input().split())))

print(nums[n])