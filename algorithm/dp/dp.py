# 재귀함수를 이용한 방식
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


# DP를 사용한 방식
def fibo_dp(n):
    cache = [0 for index in range(n+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, n+1):
        cache[index] = cache[index-1] + cache[index-2]
    return cache[index]
# 위와 같이 캐시라는 공간을 미리 할당해놓고 결과값을 계속 추가해가면서 품
# Memoization 기법


print(fibo_dp(10))