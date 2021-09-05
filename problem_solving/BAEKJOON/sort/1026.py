n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())))
count = 0

for i in range(n):
    count += a[i] * b[i]

print(count)