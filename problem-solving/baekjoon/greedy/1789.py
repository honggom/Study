s = int(input())
count = 0

for i in range(1, s):
    s -= i
    if s < 0:
        break
    count += 1

print(count)