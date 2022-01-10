# 실버 4
# 1049. 기타줄

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
package = sys.maxsize
single = sys.maxsize

for _ in range(m):
    p, s = map(int, input().split())
    package = min(package, p)
    single = min(single, s)

if package > single * 6:
    print(n * single)
else:
    a = ((n // 6) * package) + ((n % 6) * single)
    b = (((n // 6) + 1) * package)
    print(min(a, b))
