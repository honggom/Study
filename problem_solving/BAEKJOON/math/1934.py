def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    g = gcd(a, b)
    return g * (a/g) * (b/g)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(int(lcm(a, b)))


