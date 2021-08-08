question = input()
stack = []
result = ""
# A*(B+C)
# ABC+*

for x in question:
    if x.isalpha():
        result += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()
print(result)