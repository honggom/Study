'''
내 코드 : 시간초과

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visited = [False] * 10001
    q = deque()
    q.append([a, []])
    while q:
        num, cmd = q.popleft()
        visited[num] = True
        if num == b:
            break

        # Case : D
        d_num = num * 2 if num * 2 < 10000 else int((num * 2) % 10000)
        if not visited[d_num]:
            new_cmd = cmd + ["D"]
            q.append([d_num, new_cmd])

        # Case : S
        s_num = num - 1 if num != 0 else 9999
        if not visited[s_num]:
            new_cmd = cmd + ["S"]
            q.append([s_num, new_cmd])

        # Case : L
        temp_num3 = deque(list(str(num)))
        temp_num3.rotate(-1)
        l_num = int("".join(temp_num3))
        if not visited[l_num]:
            new_cmd = cmd + ["L"]
            q.append([l_num, new_cmd])

        # Case : R
        temp_num4 = deque(list(str(num)))
        temp_num4.rotate(1)
        r_num = int("".join(temp_num4))
        if not visited[r_num]:
            new_cmd = cmd + ["R"]
            q.append([r_num, new_cmd])

    print("".join(cmd))
'''
from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    q = deque()
    q.append([a, ""])
    while q:
        number, result = q.popleft()
        dn = (number * 2) % 10000
        if dn == b: return result + "D"
        elif arr[dn] == 0:
            arr[dn] = 1
            q.append([dn, result + "D"])
        sn = number - 1 if number != 0 else 9999
        if sn == b: return result + "S"
        elif arr[sn] == 0:
            arr[sn] = 1
            q.append([sn, result + "S"])
        ln = int(number % 1000 * 10 + number / 1000)
        if ln == b: return result + "L"
        elif arr[ln] == 0:
            arr[ln] = 1
            q.append([ln, result + "L"])
        rn = int(number % 10 * 1000 + number // 10)
        if rn == b: return result + "R"
        elif arr[rn] == 0:
            arr[rn] = 1
            q.append([rn, result + "R"])
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    arr = [0 for i in range(10000)]
    print(bfs())