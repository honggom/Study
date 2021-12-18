# 브론즈 1
# 6996. 애너그램

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    strs = list(input().split())
    if sorted(strs[0]) == sorted(strs[1]):
        print(f'{strs[0]} & {strs[1]} are anagrams.')
    else:
        print(f'{strs[0]} & {strs[1]} are NOT anagrams.')