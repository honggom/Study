n = sorted(list(input()), reverse=True)
sum = sum(map(int, n))
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))

'''
30의 배수가 되는 조건
1. 일의 자리수가 0 이여야 함 
2. 각 자리의 숫자들을 더한 값이 3으로 나누어 떨어져야한다.
'''