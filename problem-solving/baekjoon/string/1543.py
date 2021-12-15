# 실버 4
# 1543. 문서 검색

string = input()
s = input()
count = 0

while True:
    if s in string:
        string = string.replace(s, "*", 1)
        count += 1

    if len(s) > len(string) or string.find(s) == -1:
        break

print(count)