from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

max_num = 0
for p in permutations(nums, n):
    tmp_num = 0
    for i in range(1, n):
        tmp_num += abs(p[i - 1] - p[i])
    max_num = max(max_num, tmp_num)

print(max_num)