
data = list(input())
outPut = ''
for i in range(97, 123):
    ch = chr(i)
    if ch in data:
        outPut += (str(data.index(ch))+" ")
    else:
        outPut += "-1 "
print(outPut)
