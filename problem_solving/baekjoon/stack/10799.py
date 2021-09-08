bar_razor = list(input())
count = 0
stack = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(':
        stack.append('(')

    else:
        # 레이저인 경우
        if bar_razor[i-1] == '(': 
            stack.pop()
            count += len(stack)
        # 막대기가 끝난 경우
        else:
            stack.pop()
            count += 1

print(count)