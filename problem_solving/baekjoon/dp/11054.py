n = int(input())
nums = list(map(int, input().split()))
dp1, dp2, result = [1] * n, [1] * n, [1] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp1[i] = max(1 + dp1[j], dp1[i])

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i - 1, -1):
        if nums[i] > nums[j]:
            dp2[i] = max(1 + dp2[j], dp2[i])

for i in range(n):
    result[i] = dp1[i] + dp2[i]

print(max(result) - 1)