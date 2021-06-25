data = input().upper()
uData = list(set(data))

countList = []

for i in uData:
    countList.append(data.count(i))

if countList.count(max(countList)) > 1:
    print("?")
else:
    print(uData[countList.index(max(countList))])
