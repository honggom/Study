# data = 생성자를 통해 나온 숫자
arr = []
for i in range(1, 10000):
    nums = list(str(i))
    data = i
    for j in range(len(nums)):
        data += int(nums[j])
    arr.append(data)

for k in range(1, 10000):
    if k not in arr:
        print(k)
