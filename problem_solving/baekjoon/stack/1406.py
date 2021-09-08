# 시간초과
# from sys import stdin
# from collections import deque
#
# work_space = deque(list(stdin.readline().rstrip())+["cursor"])
#
# for _ in range(int(stdin.readline())):
#     command = stdin.readline().split()
#     cursor_index = work_space.index("cursor")
#     if command[0] == 'D' and cursor_index != len(work_space) - 1:
#         work_space[cursor_index + 1], work_space[cursor_index] = work_space[cursor_index], work_space[cursor_index + 1]
#     elif command[0] == 'L' and cursor_index != 0:
#         work_space[cursor_index - 1], work_space[cursor_index] = work_space[cursor_index], work_space[cursor_index - 1]
#     elif command[0] == 'B' and cursor_index != 0:
#         del work_space[cursor_index - 1]
#     elif len(command) == 2:
#         work_space.insert(cursor_index, command[1])
#
# [print(char, end="") for char in work_space if char != "cursor"]


from sys import stdin
work_space = list(stdin.readline().rstrip())
work_space2 = []
for _ in range(int(stdin.readline())):
    cmd = stdin.readline().split()
    if cmd[0] == 'L' and len(work_space) != 0:
        work_space2.append(work_space.pop())
    elif cmd[0] == 'D' and len(work_space2) != 0:
        work_space.append(work_space2.pop())
    elif cmd[0] == 'B' and len(work_space) != 0:
        work_space.pop()
    elif len(cmd) == 2:
        work_space.append(cmd[1])

print("".join(work_space + list(reversed(work_space2))))
