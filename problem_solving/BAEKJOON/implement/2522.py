n = int(input())
stars = []
for i in range(1, n + 1):
    star = (n - i) * " " + (i * "*")
    print(star)
    stars.append(star)
stars.pop()
for s in sorted(stars, reverse=True):
    print(s)
