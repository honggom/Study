n = int(input())
num = 0
cnt = 0
while n != cnt:
    num += 1
    if str(num).find("666") != -1:
        cnt += 1
print(num)