n = int(input())
white_space = 1
for i in range(1, n+1):
    if i == n:
        print((i * 2 - 1) * "*")
    elif i == 1:
        print((n-i) * " " + "*")
    else:
        print((n-i) * " " + "*" + (white_space * " ") + "*")
        white_space += 2