from collections import deque

ps = deque(list(input()))
stack = deque()
nums = []
for i, p in enumerate(ps):
    if p == ")":
        if ps[i-1] == "(":
            ps[i], ps[i-1] = "&", "&"
    else:
        nums.append(i)


for p in ps:
    print(p, end="")
print(nums)
'''
for i, p in enumerate(ps):
    if p == ")":
        
    else:
        stack.append(p)
    print(p, end="")
'''
