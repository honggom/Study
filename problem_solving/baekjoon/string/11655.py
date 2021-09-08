for s in input():
    if s.isupper():
        print(chr(64 + ord(s) + 13 - 90) if ord(s) + 13 > 90 else chr(ord(s) + 13), end="")
    elif s.islower():
        print(chr(96 + ord(s) + 13 - 122) if ord(s) + 13 > 122 else chr(ord(s) + 13), end="")
    else:
        print(s, end="")

