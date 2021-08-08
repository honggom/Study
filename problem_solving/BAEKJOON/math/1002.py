# 터렛
n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x2-x1)**2+(y2-y1)**2)**0.5
    R = [r1, r2, r]
    maxR = max(R)
    R.remove(maxR)
    if r == 0 and r1 == r2:
        print(-1)
    elif r == r1+r2 or maxR == sum(R):
        print(1)
    elif maxR > sum(R):
        print(0)
    else:
        print(2)
