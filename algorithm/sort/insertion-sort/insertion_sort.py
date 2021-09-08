target = [3, 2, 8, 4, 5, 1, 9, 7]


def insertion_sort(data):
    for i in range(len(data) - 1):
        for j in range(i + 1, 0, -1):
            print(data)
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
            else:
                break


insertion_sort(target)