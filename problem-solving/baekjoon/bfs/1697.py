from collections import deque
n, k = map(int, input().split())
visited = [False] * 100001
q = deque()
q.append([n, 0])

while q:
    pivot, d = q[0][0], q[0][1]
    if pivot == k:
        break
    q.popleft()
    visited[pivot] = True
    if pivot - 1 >= 0 and not visited[pivot - 1]:
        q.append([pivot - 1, d + 1])
    if pivot + 1 <= 100000 and not visited[pivot + 1]:
        q.append([pivot + 1, d + 1])
    if pivot * 2 <= 100000 and not visited[pivot * 2]:
        q.append([pivot * 2, d + 1])

print(q[0][1])