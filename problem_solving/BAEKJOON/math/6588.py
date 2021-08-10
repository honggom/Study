def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


def get_smaller_prime(num):
    if num == 3:
        return 3
    else:
        for i in range(num - 1, 2, -1):
            if is_prime(i):
                return i


def get_bigger_prime(num):
    for i in range(num + 1, 1000000):
        if is_prime(i):
            return i


# 솔루션 : 소수를 주어진 숫자 기준에서 앞, 뒤에서 동시에 구하면서 계산
while True:
    n = int(input())

    if n == 0:
        break

    front_num, back_num = 3, get_smaller_prime(n)

    while back_num >= front_num:

        sum_num = front_num + back_num

        if sum_num == n:
            print(f'{n} = {front_num} + {back_num}')
            break
        elif sum_num > n:
            back_num = get_smaller_prime(back_num)
        else:
            front_num = get_bigger_prime(front_num)
