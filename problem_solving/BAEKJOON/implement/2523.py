n = int(input())
new_n = n * 2 - 1

for i in range(1, n + 1):
    print(i * "*")
for j in range(new_n - n, -1, -1):
    print(j * "*")

