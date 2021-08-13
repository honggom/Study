import sys

n = int(input())
dp = [0] * 100001
dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 1

for i in range(5, n + 1):
    if int(i ** 0.5) ** 2 == i:
        dp[i] = 1
    else:
        if dp[i - 1] + dp[1] == 2:
            dp[i] = 2
        else:
            left, right = 1, i - 1
            count = sys.maxsize
            while left < right:
                count = min(count, dp[left] + dp[right])
                left += 1
                right -= 1
            dp[i] = count

print(dp[n])