n = input()

while n != '0':

    new = str(n[::-1])

    if (n == new):
        print('yes')
        n = input()
    else:
        print('no')
        n = input()
