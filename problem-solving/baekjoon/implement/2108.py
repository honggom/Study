import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = sorted([int(input()) for _ in range(n)])

print(round(sum(nums) / n))
print(nums[n // 2])
c = Counter(nums).most_common(2)
if len(c) > 1:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
else:
    print(c[0][0])
print(nums[-1] - nums[0])
