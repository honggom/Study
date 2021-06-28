'''
    역으로 접근해야 될 듯
    왜냐 ?
    마지막 작동은 무조건 +1 이기 때문에
    k가 어느 범위 안에 정해져 있음

    1을 포함하고 있는 k의 경우의 수는 :

    k가 0인 경우 -1 0 1
    k가 1인 경우 0 1 2
    k가 2인 경우 1 2 3

    따라서 k는 0, 1, 2
    하지만 k가 0이라면 전 이동이 없다는 의미이므로
    어차피 최소 카운트는 성립이 안돼서
    결국에 마지막 k는 1, 2

    첫 시작 이동거리는 무조건 1
    마지막 이동거리도 무조건 1

    감속과 가속을 결정하는 조건이 있어야 된다.

    base[0] 선택은 감속
    base[1] 선택은 변화 x
    base[2] 선택은 가속

# t = int(input())
# for _ in range(t):

pos = int(input())
goal = int(input())
count = 0
k = 0
base = [-1, 0, 1]

while True:
    nxt = (goal - 1) - pos
    if nxt in base and (nxt == 1 or nxt == 2):
        count += 2
        break
    else:
        if pos <= int(goal / 2) + 1:
            # 감속 시기
        else:
            # 가속 시기
            pos += base[2]
            k = base[2]
            base = [k-1, k, k+1]
            count += 1

print(count)


# 감속시기를 찾는 방법 ?..
# 우선 증가가 아닌 것 부터

# ...결국 실패
# k가 포물선 형태라는 것은 알아냄
# 하지만 거리수에 따른 경우의 수를 정리해보며 하진 않았다.
# 답은 경우의 수를 적은 필기를 보고 알 수 있었음..
# 하지만 봤다고 규칙을 찾았을지는 미지수 .. 

'''

import math

for tc in range(int(input())):
    x, y = map(int, input().split())
    dist = y - x  # 실 이동 거리
    sq = int(math.sqrt(dist))  # 제곱근
    etc = dist - sq ** 2  # 나머지
    count = sq * 2 - 1
    if etc == 0:
        print(count)
    elif etc <= sq:
        print(count + 1)
    else:
        print(count + 2)
