```python
# 최대 공약수 (재귀)
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
# 최대 공약수 (반복문)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최대 공약수 (모듈)
from math import gcd
print(gcd(a, b))
    
# 최소 공배수 
def lcm(a, b):
    g = gcd(a, b)
    return int(g * (a/g) * (b/g))

# 소수
def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
```