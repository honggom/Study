import sys
input = sys.stdin.readline

n = int(input())

ts = []
ps = []
dp = []

for _ in range(n):
    t, p = map(int, input().split())
    ts.append(t)
    ps.append(p)
    dp.append(p)
dp.append(0)

for i in range(n - 1, -1, -1):
    if ts[i] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], ps[i] + dp[i + ts[i]])
        # 상담을 안 하는 것 : dp[i + 1] // 상담을 하는 것 ps[i] + dp[i + ts[i]] 중 큰 값을 저장

print(dp[0])