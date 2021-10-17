def solution(p, s):
    import math

    answer = []

    day = math.ceil((100 - p[0]) / s[0])
    start = 0
    _sum = 0

    while _sum != len(p):

        count = 0

        for i in range(start, len(p)):
            if p[i] + (day * s[i]) >= 100:
                count += 1
                _sum += 1
            else:
                day = math.ceil((100 - p[i]) / s[i])
                start = i
                break

        answer.append(count)

    return answer