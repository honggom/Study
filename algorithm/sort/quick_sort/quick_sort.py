target = [6, 7, 1, 2, 6, 1, 1, 5, 5, 6, 10, 123, 5451, 3123, 5, 1, 2, 3123, 423123, 4123, 1234]


def quick_sort(data):
    if len(data) <= 1:
        return data
    left, right = list(), list()
    pivot = data[0]
    for i in range(1,len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


# 파이써닉하게
def quick_sort2(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort(target))