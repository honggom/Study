# 골드 4
# 9935. 문자열 폭발

import sys
input = sys.stdin.readline

target = list(input().rstrip())
bomb = list(input().rstrip())

stack = []

for i in range(len(target)):
    stack.append(target[i])
    bomb_len = len(bomb)

    if stack[-1] == bomb[-1] and len(stack) >= bomb_len and stack[-bomb_len:] == bomb:
        [stack.pop() for _ in range(bomb_len)]

if stack:
    print(''.join(stack))
else:
    print('FRULA')

# 시간 초과 ^^
# import sys
# input = sys.stdin.readline
#
# target = input().rstrip()
# bomb = input().rstrip()
#
# while target != '' and target.find(bomb) != -1:
#     target = target.replace(bomb, '')
#
# if target == '':
#     print('FRULA')
# else:
#     print(target)