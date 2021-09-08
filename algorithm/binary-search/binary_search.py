def binary_search(data, search):
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    mid = len(data) // 2
    if search == data[mid]:
        return True
    else:
        if search > data[mid]:
            print(data)
            return binary_search(data[mid:], search)
        else:
            print(data)
            return binary_search(data[:mid], search)


data = [1,2,3,4,5,6,7,8,9,10,11]
binary_search(data,8)
