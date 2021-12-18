# 브론즈 2
# 5598. 카이사르 암호

for c in list(input()):
    if c == 'A':
        print('X', end='')
    elif c == 'B':
        print('Y', end='')
    elif c == 'C':
        print('Z', end='')
    else:
        print(chr(ord(c) - 3), end='')