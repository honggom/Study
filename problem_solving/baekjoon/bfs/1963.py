from collections import deque
import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def check(num, index, depth):
    global q
    pivot = list(str(num))
    del pivot[index]
    for i in range(10):
        pivot.insert(index, str(i))
        changed_num = int("".join(pivot))
        if changed_num >= 1000 and primes[changed_num] and not visited[changed_num]:
            q.append([changed_num, depth])
        del pivot[index]

primes = [is_prime(i) for i in range(10000)]
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    visited = [False] * 10000
    q = deque()
    q.append([n, 0])
    while q:
        num, depth = q.popleft()
        visited[num] = True
        if num == m:
            print(depth)
            break
        else:
            for i in range(4):
                check(num, i, depth + 1)