from collections import Counter

nums = [int(input()) for _ in range(10)]

print(int(sum(nums) / 10))
print(Counter(nums).most_common(1)[0][0])