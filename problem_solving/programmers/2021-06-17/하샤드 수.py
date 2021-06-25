def solution(x):
    return x % sum([int(num) for num in str(x)]) == 0




