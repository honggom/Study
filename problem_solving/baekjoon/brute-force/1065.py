# 한수 구하기
# 한수 == 각 자리수들이 등차수열을 이루는 수
data = int(input())
count = 0

for index in range(data):
    if index+1 < 100:
        count += 1
    elif index+1 != 1000:
        a, b, c = map(int, list(str(index+1)))
        if (c - b) == (b - a):
            count += 1
print(count)
