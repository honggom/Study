tn = int(input())


for _ in range(tn):
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
    else:
        p = 0
        for i in range(n):
            if i == 1:
                n = k + 2
        print(p)
