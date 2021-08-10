def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n, s = map(int, input().split())
distance = [abs(p-s) for p in list(map(int, input().split()))]
min_num = min(distance)

if s == 1:
    print(distance[0])
else:
    for i in range(len(distance)):
        min_num = gcd(distance[i], min_num)
    print(min_num)