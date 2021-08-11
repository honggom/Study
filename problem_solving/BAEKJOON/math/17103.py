def is_prime(num):
    if num == 1 or num == 0:
        return False
    else:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                return False
        return True


primes = [is_prime(i) for i in range(1000001)]
t = int(input())

for _ in range(t):
    n = int(input())
    left, right = 0, n
    count = 0

    while left <= right:

        while not primes[left]:
            left += 1
        while not primes[right]:
            right -= 1

        sum_num = left + right

        if sum_num == n:
            count += 1
            right -= 1
        elif sum_num > n:
            right -= 1
        else:
            left += 1

    print(count)