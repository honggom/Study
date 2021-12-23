# 실버 5
# 1439. 뒤집기

s = list(input().rstrip())

stack = [s[0]]
one = zero = 0

for i in range(1, len(s)):
    if stack[-1] != s[i]:
        while stack:
            p = stack.pop()
        if p == '0':
            zero += 1
        else:
            one += 1
    stack.append(s[i])

if stack:
    if stack[-1] == '0':
        zero += 1
    else:
        one += 1

print(min(one, zero))