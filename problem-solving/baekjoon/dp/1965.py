# 실버 2
# 1965. 상자넣기

import sys
input = sys.stdin.readline

n = int(input().rstrip())
boxes = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))