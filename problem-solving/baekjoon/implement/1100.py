mtx = []
odd = True
ans = 0

for _ in range(8):
    mtx.append(list(input().rstrip()))

for i in range(8):
    if odd:
        for j in range(0, 8, 2):
            if mtx[i][j] == "F":
                ans += 1
        odd = False
    else:
        for k in range(1, 8, 2):
            if mtx[i][k] == "F":
                ans += 1
        odd = True

print(ans)

