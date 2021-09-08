 # 분수 찾기 문제
# key point :
# 1. 몇번째 대각선인지..
# 2. 대각선이 좌/우측 어디로 향하고 있는지
# crossNum : 몇번째 대각선인지 알려주는 변수
# check : 해당 대각선의 최대 번호

crossNum = 1
counter = 2
check = 1
n = 0

for _ in range(int(input())):
    n += 1
    if check < n:
        check += counter
        counter += 1
        crossNum += 1
down = crossNum
up = 1

# 우측으로 향하는 대각선의 경우
if crossNum % 2 == 1:
    for _ in range(check - n):
        up += 1
        down -= 1

# 좌측으로 향하는 대각선의 경우
else:
    tmp = up
    up = down
    down = tmp
    for _ in range(check - n):
        up -= 1
        down += 1
print("%d/%d" % (up, down))
