'''
1 ~ 9 : 9개
10 ~ 99 : 180개
100 ~ 999 : 2700개
1000 ~ 9999 : 36000개

: 9 * 10 ** i * (i + 1)
'''
n = int(input())
n_len = len(str(n))
count = 0

# 자리수 기반으로 개수를 구함
for i in range(n_len - 1):
    count += 9 * 10 ** i * (i + 1)

# 자리수를 구하고 나머지 숫자를 구하고 출력
print(count + (n - 10 ** (n_len - 1) + 1) * n_len)
