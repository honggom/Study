import sys

n = int(input())
d = str(n)
count = 0

if n < 10:
    d = "0" + str(n)

while True:
    length = len(d)-1
    d2 = str(int(d[0])+int(d[1]))
    length2 = len(d2)-1
    d = d[length] + d2[length2]
    count += 1
    if int(d) == n:
        print(count)
        break
