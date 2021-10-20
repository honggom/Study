from collections import deque
import sys
input = sys.stdin.readline
# 입력 1   0   1   0   1   1   1   1
# 시간 12  1   3   5   6   7   9   11
# idx 0  1    2   3   4   5   6   7
# rotate(1) ==> 시계 방향
# rotate(-1) ==> 반 시계

r1 = deque(list(map(int, list(input().rstrip()))))
r2 = deque(list(map(int, list(input().rstrip()))))
r3 = deque(list(map(int, list(input().rstrip()))))
r4 = deque(list(map(int, list(input().rstrip()))))
r = [r1, r2, r3, r4]
n = int(input())
revers = {1 : -1, -1 : 1}
checkd = [False] * 4

temp = []

def turn(target, direc, left, right):
    if target < 0 or target > 3:
        return
    checkd[target] = True
    temp.append([target, direc])

    if 0 < target < 3 and left != r[target - 1][2] and not checkd[target]:
        turn(target - 1, revers[direc], r[target - 1][6], r[target - 1][2])

    if 0 < target < 3 and right != r[target + 1][6] and not checkd[target]:
        turn(target + 1, revers[direc], r[target - 1][6], r[target - 1][2])

for _ in range(n):
    target, direc = map(int, input().split())
    turn(target - 1, direc, r[target - 1][6], r[target - 1][2])

    for t in temp:
        r[t[0]].rotate(t[1])

    temp.clear()
    for i in range(4):
        checkd[i] = False

cnt = 0

if r1[0] == 1:
    cnt += 1
if r2[0] == 1:
    cnt += 2
if r3[0] == 1:
    cnt += 4
if r4[0] == 1:
    cnt += 8

print(cnt)
