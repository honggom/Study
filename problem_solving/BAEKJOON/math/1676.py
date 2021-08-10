def fac(num):
    if num == 1 or num == 0:
        return 1
    return num * fac(num - 1)

num = str(fac(int(input())))
count = 0

for i in range(len(num) - 1, -1, -1):
    if num[i] != "0":
        print(count)
        break
    else:
        count += 1