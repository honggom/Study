from itertools import combinations

n = int(input())
nums = []

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str, comb))))

try:
    print(sorted(nums)[n])
except:
    print(-1)