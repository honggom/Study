'''
동전 문제 :
    지불해야 하는 값이 n 원일때 1원 50원 100원 500원 동전으로 동전의 수가 가장 적게 지불하시오
    -> 이때 동전의 수를 구한다.
'''

coin_list = [500, 100, 50, 1]


def min_coin_count(n, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = n // coin
        total_coin_count += coin_num
        n -= coin * coin_num
        details.append([coin, coin_num])
    return total_coin_count, details


a, b = min_coin_count(4720, coin_list)
print(a, b)

