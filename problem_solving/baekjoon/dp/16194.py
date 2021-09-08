import sys
n = int(input())
prices = [0] + list(map(int, input().split()))
cache = [0] + [sys.maxsize] * n
cache[1] = prices[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        cache[i] = min(cache[i], cache[i - j] + prices[j])

print(cache[n])
