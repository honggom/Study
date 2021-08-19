for _ in range(int(input())):
    n = int(input())

    dp = [0] * 101
    dp[1], dp[2], dp[3] = 1, 1, 1
    dp[4], dp[5] = 2, 2

    for i in range(6, n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[n])