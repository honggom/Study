string = input()
strings = []
for i in range(len(string)):
    strings.append(string[i:])

[print(s) for s in sorted(strings)]