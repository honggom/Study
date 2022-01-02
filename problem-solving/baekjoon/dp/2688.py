# 골드 5
# 2688. 줄어들지 않아

for i in range(int(input())):
    n = int(input())
    dp = [1 for i in range(10)]

    for i in range(n-1):
        for j in range(10):
            dp[j] = sum(dp[j:])
    print(sum(dp))