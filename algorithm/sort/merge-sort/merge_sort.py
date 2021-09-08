def merge_sort(data):
    return split(data)


def split(data):
    if len(data) <= 1:
        return data
    mid = int(len(data)/2)
    left = split(data[:mid])
    right = split(data[mid:])
    return merge(left, right)


def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case 1: left/right가 아직 남아있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case 2: left만 남아있을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    # case 3: right만 남아있을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


target = [10,7,1,5,6,8,1,2,3]

# print(merge-sort(target))

def split2(data):
    if len(data) <= 1:
        return data
    mid = int(len(data)/2)
    left = split(data[:mid])
    right = split(data[mid:])
    return left, right

print(split(target))