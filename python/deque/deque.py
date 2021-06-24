from collections import deque

dq = deque([1, 2, 3, 4, 5])

print(dq)
print(dq.popleft())
print(dq)
dq.appendleft(1)
print(dq)
dq.append(13)
print(dq)
print(dq.pop())
print(dq)


'''
결과 : 
deque([1, 2, 3, 4, 5])
1
deque([2, 3, 4, 5])
deque([1, 2, 3, 4, 5])
deque([1, 2, 3, 4, 5, 13])
13
deque([1, 2, 3, 4, 5])
'''