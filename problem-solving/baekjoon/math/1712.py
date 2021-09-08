a, b, c = map(int, input().split())

if b > c or b == c:
    print(-1)
else:
    c = c - b
    print(int(a/c) + 1)
