import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start = ""
for _ in range(3):
    temp = input().strip()
    temp = temp.replace(" ", "")
    start += temp

start = start.replace("0", "9")

q = deque()
q.append(start)

count = dict()
count[start] = 0

while q:
    now = q.popleft()
    if now == "123456789":
        print(count[now])
        sys.exit(0)

    pos = now.find("9")
    x = pos // 3 # 몫
    y = pos % 3  # 나머지

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_pos = new_x * 3 + new_y
            next_num = list(now)
            next_num[new_pos], next_num[pos] = next_num[pos], next_num[new_pos]
            next_num = "".join(next_num)

            if not count.get(next_num):
                q.append(next_num)
                count[next_num] = count[now] + 1

print("-1")