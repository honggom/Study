# 시간초과
'''
class Solution:
    def dailyTemperatures(self, temperatures):
        l = temperatures
        rtn = [0] * len(l)
        pointer = 0

        while len(l) != pointer + 1:
            for t in range(pointer + 1, len(l)):
                if l[t] > l[pointer]:
                    rtn[pointer] = t - pointer
                    break
            pointer += 1

        return rtn
'''

class Solution:
    def dailyTemperatures(self, T):
        answer = [0] * len(T)
        stack = []

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
