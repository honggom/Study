answer = 0

def solution(numbers, target):
    global answer

    def dfs(index, num):
        global answer
        if index == len(numbers):
            if num == target:
                answer += 1
            return

        dfs(index + 1, num + numbers[index])
        dfs(index + 1, num - numbers[index])

    dfs(0, 0)

    return answer