from collections import deque

string = deque(list(input()))
stack = []
result = ""

while string:
    if string[0] == '<':
        while string[0] != '>':
            result += string.popleft()
        result += string.popleft()
    elif string[0] == " ":
        result += string.popleft()
    else:
        while len(string) > 0 and string[0] != "<" and string[0] != " ":
            stack.append(string.popleft())
        while stack:
            result += stack.pop()

print(result)