# 실버 1
# 1309. 동물원

n = int(input())

dp = [0] * 100001
dp[1] = 3
dp[2] = 7

for i in range(3, 100001):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(dp[n])