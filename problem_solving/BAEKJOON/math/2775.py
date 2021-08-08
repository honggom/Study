# 부녀회장 문제
tc = int(input())

for _ in range(tc):
    k = int(input())
    n = int(input())
    base = [j for j in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            base[i] = base[i] + base[i-1]
            # 여기가 포인트
            # 할당되기전에 그 수가 존재한다는게 포인트
            # 규칙까지는 구했는데 코드로 옮기는데 어려움이 있었다..
    print(base[n-1])
