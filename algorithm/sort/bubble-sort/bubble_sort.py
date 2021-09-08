target = [5, 9, 8, 7, 6, 10, 4, 3, 2, 1]


def bubble_sort(data):
    # 리스트의 마지막 요소까지 접근할 필요가 없음
    # Why? index에서 index + 1까지 접근하여 정렬하기 때문
    # 따라서 바깥 loop는 len(list) - 1
    for i in range(len(data) - 1):
        swap = False
        # 바깥쪽 index인 i를 빼줌
        # Why? 안쪽 loop를 돌때 마다 최소 하나의 값은 정렬이 보장되기 때문
        for j in range(len(data) - i - 1):
            print(f'list = {data}, i = {i}, j = {j}, len = {len(data) - i - 1}')
            if data[j] > data[j+1]:
                data[j+1], data[j] = data[j], data[j+1]
                swap = True

        # 안쪽 for 문을 한 바퀴 돌면서 바뀐게 없으면 이미 정렬된 것이므로 탈출
        if not swap:
            break


bubble_sort(target)
print(target)