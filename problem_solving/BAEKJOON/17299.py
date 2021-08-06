from collections import Counter
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
count_num = Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and count_num[nums[stack[-1]]] < count_num[nums[i]]:
            result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)