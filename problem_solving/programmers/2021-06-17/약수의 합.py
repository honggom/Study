def solution(n):
    return sum([c for c in range(1, n**2+1) if n % c == 0])
