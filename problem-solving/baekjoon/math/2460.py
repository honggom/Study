count, mx = 0, 0

for _ in range(10):
    _out, _in = map(int, input().split())
    count -= _out
    count += _in
    mx = max(mx, count)

print(mx)