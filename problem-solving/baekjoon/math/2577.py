import sys
a = int(input())
b = int(input())
c = int(input())

for i in range(10):
    print(list(str(a * b * c)).count(str(i)))
