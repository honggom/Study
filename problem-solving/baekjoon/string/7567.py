# 브론즈 2
# 7567. 그릇

s = list(input().rstrip())

count = 10

for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        count += 5
    else:
        count += 10

print(count)