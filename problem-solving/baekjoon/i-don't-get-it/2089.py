num = int(input())
binary = ''

if not num:
    print(0)
else:
    while num:
        if num % -2:
            binary = '1' + binary
            num = num // -2 + 1
        else:
            binary = '0' + binary
            num = num // -2

print(binary)