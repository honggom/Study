import sys
stack = []

for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()

    if len(cmd) == 2:
        stack.append(cmd[1])
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            data = stack[-1]
            del stack[-1]
            print(data)








