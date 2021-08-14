# 6번 문제 : 성공
def solution6(numOfStairs):
    dp = [1, 2, 4]
    n = numOfStairs

    if len(dp) < n:
        dp = list(dp + [0 for i in range(n - len(dp))])

    for j in range(n):
        if dp[j] == 0:
            dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3]

    return dp[n - 1]

# 5번 문제 : 시간 초과
def solution5(fruitWeights, k):
    n = 0
    result = set()
    max_len = len(fruitWeights) + 1

    while True:
        result.add(max(fruitWeights[n:k]))
        n += 1
        k += 1
        if k == max_len:
            break

    return sorted(result, reverse=True)

