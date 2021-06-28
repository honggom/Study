from math import ceil
testCase = int(input())

floor = 0

for _ in range(testCase):
    height, width, n = map(int, input().split())
    roomNum = ceil(n / height)
    for _ in range(n):
        floor += 1
        if floor > height:
            floor = 1
    if roomNum < 10:
        roomNum = "0"+str(roomNum)
    print("%d%s" % (floor, roomNum))
    floor = 0
