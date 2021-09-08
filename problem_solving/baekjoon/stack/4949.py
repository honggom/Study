while True:
    string = input()
    if string == '.':
        break
    stack = []
    flag = True
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if not stack or stack[-1] == '[':
                flag = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif s == ']':
            if not stack or stack[-1] == '(':
                flag = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if flag and not stack:
        print('yes')
    else:
        print('no')