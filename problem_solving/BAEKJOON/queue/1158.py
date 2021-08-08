from collections import deque
n, k = map(int, input().split())
dq = deque([i+1 for i in range(n)])

result = []
while dq:
    dq.rotate(-(k-1))
    result.append(dq.popleft())
print("<", end="")
[print(result[i], end=", ") for i in range(len(result)) if i != len(result) - 1]
print(str(result[len(result)-1])+">")
