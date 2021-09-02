from collections import deque
n, k = map(int, input().split())
visited = [0 for i in range(100001)]
q = deque()
q.append([n, 0])

while q:
    pivot, d = q[0][0], q[0][1]
    if pivot == k:
        break
    q.popleft()
    visited[pivot] = 1
    if pivot - 1 >= 0 and visited[pivot - 1] == 0:
        q.append([pivot - 1, d + 1])
    if pivot + 1 <= 100000 and visited[pivot + 1] == 0:
        q.append([pivot + 1, d + 1])
    if pivot * 2 <= 100000 and visited[pivot * 2] == 0:
        q.append([pivot * 2, d + 1])

print(q[0][1])