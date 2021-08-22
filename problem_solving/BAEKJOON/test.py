buttons = [i for i in range(10)]

def is_nearest_num(num):
    nums = list(str(num))
    is_all_nums_exist = True

    for i in nums:
        if int(i) not in buttons:
            is_all_nums_exist = False

    if is_all_nums_exist:
        return True
    else:
        return False

print(is_nearest_num(-1))