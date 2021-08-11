n = int(input())

cache = [0, 1, 3, 5]

for i in range(4, 1001):
    cache.append((cache[i - 2] * 2) + cache[i - 1])

print(cache[n] % 10007)