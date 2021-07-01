strs = input()
start = 0
end = 10
for i in range(int(len(strs) / 10) +1):
    print(strs[start:end])
    start += 10
    end += 10