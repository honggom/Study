def solution(array, commands):
    answer = []
    for val in commands:
        answer.append(sorted(array[val[0] - 1:val[1]])[val[2] - 1])
    return answer
