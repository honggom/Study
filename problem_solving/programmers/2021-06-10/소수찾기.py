def getPrime(num):
    count = 0
    for i in range(2, num+1):
        isPrime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            count += 1
    return count


def solution(n):
    answer = getPrime(n)
    return answer
