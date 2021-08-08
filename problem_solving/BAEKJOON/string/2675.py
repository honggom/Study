caseNum = int(input())

for _ in range(caseNum):
    n, d = input().split()
    b = ""
    for c in d:
        b += c*int(n)
    print(b)
