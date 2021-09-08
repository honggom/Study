def solution(a, b):
    l = [a,b]
    c = 0
    for n in range(min(l), max(l)+1):
        c += n
    return c

