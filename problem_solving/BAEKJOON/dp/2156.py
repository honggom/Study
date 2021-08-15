t = int(input())
wines = [0] + [int(input()) for _ in range(t)]
dp = [0] + [wines[1]]

if t > 1:
    dp.append(wines[1] + wines[2])

for i in range(3, t + 1):
    case1 = dp[i - 1]                           # 이번 포도주를 안 먹는 경우
    case2 = wines[i] + dp[i - 2]                # 이번 포도주를 먹고 저번 포도주를 안 먹는 경우
    case3 = wines[i] + wines[i - 1] + dp[i - 3] # 이번 포도주를 먹고 저번 포도주를 먹는 경우
    dp.append(max(case1, case2, case3))

print(dp[t])