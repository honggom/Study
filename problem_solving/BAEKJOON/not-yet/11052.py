n = int(input())
cache = [0] * (n + 1)
prices = [0] + list(map(int, input().split()))
cache[1] = prices[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        if cache[i] < cache[i - j] + prices[j]:
            cache[i] = cache[i - j] + prices[j]

print(cache[n])