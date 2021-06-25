# 설탕 배달
n = int(input())
c3 = 0

if n % 5 == 0:
    print(n // 5)
else:
    while True:
        if n - 5 < 0 and n - 3 < 0:
            print(-1)
            break
        else:
            n -= 3
            c3 += 1
            if n % 5 == 0:
                print(c3 + (n // 5))
                break
