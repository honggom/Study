'''
0 : 0
1 : 1
2 : 1
3 : 2
4 : 3
5 : 5
6 : 8
'''

n = int(input())
cache = [0, 1, 1, 2]

for i in range(4, 101):
    cache.append(cache[i - 1] + cache[i - 2])

print(cache[n])