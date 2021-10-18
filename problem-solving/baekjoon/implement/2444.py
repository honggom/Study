n = int(input())

tail = []

for i in range(1, n + 1):
    star = (n - i) * " " + ((i * 2) - 1) * "*"

    if i != n:
        tail.append(star)

    print(star)

[print(s) for s in reversed(tail)]