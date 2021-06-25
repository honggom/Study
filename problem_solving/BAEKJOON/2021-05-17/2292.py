data = int(input())
tmp = 1
num = 6
count = 1

while tmp <= data:
    if data == 1:
        break
    tmp += num
    num += 6
    count += 1

tmp = 1
num = 6
for _ in range(count-2):
    tmp += num
    num += 6

if tmp == data and data != 1:
    count -= 1

print(count)
