import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

left = 1
right = houses[-1] - houses[0]
result = 0

while left <= right:
    mid = (left + right) // 2 # 설치 간격
    set_position = houses[0]  # 설치 장소
    count = 1

    for house in houses:
        if house >= set_position + mid:
            count += 1
            set_position = house

    if count >= c:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)