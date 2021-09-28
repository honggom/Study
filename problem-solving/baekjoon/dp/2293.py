n, k = map(int, input().split())
coins = []
dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in range(n):
    coins.append(int(input()))

for coin in coins:
    for index in range(1, k + 1):
        if index - coin >= 0:
            dp[index] += dp[index - coin]

print(dp[k])