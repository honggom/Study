target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def selection_sort(target):

    # 10개의 데이터가 있는 리스트는 최대 9번의 정렬이면 정렬됨
    # 따라서 i는 range는 len - 1
    for i in range(len(target) - 1):
        # 제일 작은 값을 갖는 데이터의 index를 나타냄
        min_index = i


        # min_index의 값보다 작은 것이 있으면 반복하면서 할당해줌
        for j in range(i+1, len(target)):
            if target[min_index] > target[j]:
                min_index = j
        target[min_index], target[i] = target[i], target[min_index]


selection_sort(target)
print(target)