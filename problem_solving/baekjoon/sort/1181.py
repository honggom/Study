from sys import stdin
chars = set()
for _ in range(int(stdin.readline())):
    chars.add(stdin.readline().rstrip())
chars = sorted(list(chars), key=lambda s : (len(s), s))
for val in chars:
    print(val)