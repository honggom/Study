def fac(n):
    if n > 1:
        return n * fac(n - 1)
    else:
        return 1

def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

def magic(n):
    if n == 1:
        return
    if n % 2 == 0:
        print(n)
        magic(int(n / 2))
    else:
        print(n)
        magic(n * 3 + 1)


magic(3)