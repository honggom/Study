def solution(n):
    return '수' if n == 1 else '수박' if n == 2 else '수박' * int(n/2) if n % 2 == 0 else '수박' * int(n/2) + '수'
