# 브론즈 2
# 10996. 별 찍기 - 21

n = int(input())

for i in range(1, n * 2 + 1):
    if i % 2 == 0:
        for k in range(1, n + 1):
            if k % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
    else:
        for k in range(1, n + 1):
            if k % 2 != 0:
                print("*", end="")
            else:
                print(" ", end="")
    print()