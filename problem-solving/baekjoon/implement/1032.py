import sys
input = sys.stdin.readline

t = int(input())
strings = []

for _ in range(t):
    strings.append(list(input().rstrip()))

length = len(strings[0])
result = ""

for i in range(length):
    cur_chr = None
    isRight = True

    for string in strings:
        if not cur_chr:
            cur_chr = string[i]
        else:
            if cur_chr != string[i]:
                isRight = False

    if isRight:
        result += string[i]
    else:
        result += "?"

print(result)