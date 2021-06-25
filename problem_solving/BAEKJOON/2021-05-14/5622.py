data = list(map(ord, input().upper()))
data = [num - 64 for num in data]

count = 0

for i in data:
    if i > 0 and i < 4:
        count += 3
    elif i > 3 and i < 7:
        count += 4
    elif i > 6 and i < 10:
        count += 5
    elif i > 9 and i < 13:
        count += 6
    elif i > 12 and i < 16:
        count += 7
    elif i > 15 and i < 20:
        count += 8
    elif i > 19 and i < 23:
        count += 9
    elif i > 22 and i < 27:
        count += 10
    else:
        count += 11
        
print(count)
