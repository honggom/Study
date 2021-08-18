n = int(input())
steps = [0 for i in range(301)]

for i in range(n):
    steps[i] = int(input())

dp = [steps[0]] + [0 for i in range(300)]
dp[1] = steps[0] + steps[1]
dp[2] = max(steps[1] + steps[2], steps[0] + steps[2])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + steps[i - 1] + steps[i], dp[i - 2] + steps[i])

print(dp[n - 1])
