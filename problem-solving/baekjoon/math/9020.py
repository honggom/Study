# 골드바흐의 추측
import sys


def getPrime(num):
    primeList = []
    for i in range(2, num):
        isPrime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(i)
    return primeList


for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    primeList = getPrime(n)
    check = []
    if int(n / 2) in primeList:
        print("%d %d" % (n/2, n/2))
    else:
        for a in primeList:
            if n - a in primeList:
                if abs((n-a)-a) not in check:
                    check.append(abs((n-a)-a))
                else:
                    print(n-a, a)
                    break
