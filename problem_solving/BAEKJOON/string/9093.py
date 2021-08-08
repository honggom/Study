strings = []
for _ in range(int(input())):
    strings.append(input())

for string in strings:
    chars = string.split()
    for char in chars:
        print("".join(reversed(list(char))), end=" ")
    print()



