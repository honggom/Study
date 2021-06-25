n = input()
tmpStr = ""
count = 0

for _ in range(int(n)):
    data = input()
    for s in data:
        if len(data) == 1:
            count += 1
        else:
            if tmpStr.find(s) == -1:
                tmpStr += s
            else:
                if s != tmpStr[len(tmpStr)-1]:
                    tmpStr = ""
                else:
                    tmpStr += s
    if len(data) == len(tmpStr):
        count += 1
    tmpStr = ""
print(count)
