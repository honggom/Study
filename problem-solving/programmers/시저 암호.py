def solution(s, n):
    rtn = []
    for c in s:
        if c == ' ':
            rtn.append(' ')
        else:
            od = ord(c) + n
            if c.isupper():
                if od > 90:
                    rtn.append(chr(od - 90 + 64))
                else:
                    rtn.append(chr(od))
            else:
                if od > 122:
                    rtn.append(chr(od - 122 + 96))
                else:
                    rtn.append(chr(od))
    return ''.join(rtn)
