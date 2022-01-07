# 브론즈 2
# 5585 거스름돈

n = int(input())
coins = [500, 100, 50, 10, 5, 1]
target = 1000 - n
count = 0

for coin in coins:
    c = int(target / coin)
    count += c
    target = target - (c * coin)

print(count)