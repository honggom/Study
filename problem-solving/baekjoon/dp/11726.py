n = int(input())
cache = [0, 1, 2]

for i in range(3, 1001):
  cache.append(cache[i - 2] + cache[i - 1])

print(cache[n] % 10007)