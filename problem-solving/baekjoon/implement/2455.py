cur = 0
result = 0

for _ in range(4):
    _out, _in = map(int, input().split())
    cur += _in
    cur -= _out
    result = max(result, cur)

print(result)