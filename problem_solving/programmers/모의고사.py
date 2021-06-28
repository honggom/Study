def solution(answers):
    answer = [0, 0, 0]
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ac1 = 0
    ac2 = 0
    ac3 = 0
    for i in answers:
        if a1[ac1] == i:
            answer[0] = answer[0] + 1
        if a2[ac2] == i:
            answer[1] = answer[1] + 1
        if a3[ac3] == i:
            answer[2] = answer[2] + 1
        ac1 += 1
        ac2 += 1
        ac3 += 1
        if ac1 == len(a1):
            ac1 = 0
        if ac2 == len(a2):
            ac2 = 0
        if ac3 == len(a3):
            ac3 = 0
    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i + 1)
    return result