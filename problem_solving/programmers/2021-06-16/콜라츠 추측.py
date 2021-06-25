count = 0


def solution(num):
    global count
    if num == 1:
        return 0
    else:
        count += 1
        if num % 2 == 0:
            solution(num/2)
        else:
            solution(num * 3 + 1)
    return count if count < 500 else -1


