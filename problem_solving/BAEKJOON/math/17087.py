def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n, s = map(int, input().split())
distance = [abs(p-s) for p in list(map(int, input().split()))]
min_dist = min(distance)

for i in range(len(distance)):
    min_dist = gcd(distance[i], min_dist)
print(min_dist)