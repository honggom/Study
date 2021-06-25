import sys
a, b = map(int, sys.stdin.readline().split())

if a == 1 and b == 1:
    print(1)
    print(1)
elif a == 1:
    print(1)
    print(b)
elif b == 1:
    print(1)
    print(a)
else:
    def mag(n):
        arr = []
        while n != 1:
            for i in range(2, n+1):
                if n % i == 0:
                    n = int(n / i)
                    arr.append(i)
                    break
        return arr

    al = mag(a)
    bl = mag(b)

    used = []
    lcm = 1
    for i in range(len(al)):
        if al[i] not in used:
            if al.count(al[i]) >= bl.count(al[i]):
                lcm *= al[i] ** al.count(al[i])
            else:
                lcm *= al[i] ** bl.count(al[i])
            if al[i] not in used:
                used.append(al[i])

    for j in range(len(bl)):
        if bl[j] not in used:
            if bl.count(bl[j]) >= al.count(bl[j]):
                lcm *= bl[j] ** bl.count(bl[j])
            else:
                lcm *= bl[j] ** al.count(bl[j])
            if bl[j] not in used:
                used.append(bl[j])

    num = 0
    if a >= b:
        num = a
    else:
        num = b

    gcd = 1

    check = True
    while check:
        for k in range(2, num+1):
            if a % k == 0 and b % k == 0:
                gcd *= k
                a = int(a / k)
                b = int(b / k)
            else:
                check = False
        print(gcd)
        print(lcm)
