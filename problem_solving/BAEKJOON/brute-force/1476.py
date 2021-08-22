e, s, m = map(int, input().split())
s1, s2, s3, year = 1, 1, 1, 1

while e != s1 or s != s2 or m != s3:
    s1 += 1; s2 += 1; s3 += 1; year += 1
    if s1 > 15:
        s1 = 1
    if s2 > 28:
        s2 = 1
    if s3 > 19:
        s3 = 1

print(year)