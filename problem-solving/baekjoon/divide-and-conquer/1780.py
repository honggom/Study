import sys
input = sys.stdin.readline

n = int(input())
mtx = [list(map(int, input().split())) for _ in range(n)]
m, z, o = 0, 0, 0

def check(x, y, length):
    global m, z, o
    for i in range(x, x + length):
        for j in range(y, y + length):
            if mtx[x][y] != mtx[i][j]:
                for a in range(3):
                    for b in range(3):
                        check(x + length // 3 * a, y + length // 3 * b, length // 3)
                return

    if mtx[x][y] == -1:
        m += 1
    elif mtx[x][y] == 0:
        z += 1
    elif mtx[x][y] == 1:
        o += 1

check(0, 0, n)
print(m)
print(z)
print(o)