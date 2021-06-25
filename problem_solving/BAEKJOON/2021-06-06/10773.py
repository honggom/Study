arr = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        del arr[-1]
    else:
        arr.append(n)
print(sum(arr))
