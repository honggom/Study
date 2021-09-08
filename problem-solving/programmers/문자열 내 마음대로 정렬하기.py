def solution(strs, n):
    return sorted(strs, key=lambda x : (x[n], x))