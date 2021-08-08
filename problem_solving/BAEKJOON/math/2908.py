a, b = list(map(list, input().split()))
a.reverse()
b.reverse()
c = int(a[0]+a[1]+a[2])
d = int(b[0]+b[1]+b[2])

if c > d:
    print(c)
else:
    print(d)
