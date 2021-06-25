arr = []
for i in range(9):
    arr.append(int(input()))
tmp = arr[:]
arr.sort()
print(arr[8])
print(tmp.index(arr[8])+1)
# tmp = arr -> 이런식으로 하면 같은 주소를 사용함.. 첨 알았다..
