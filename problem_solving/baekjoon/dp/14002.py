n = int(input())
nums = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(dp)

result = []
max_num_dp = max(dp)

print(max_num_dp)

for i in range(len(dp)-1, -1, -1):
    if dp[i] == max_num_dp:
        result.append(nums[i])
        max_num_dp -= 1

[print(i, end=" ") for i in reversed(result)]