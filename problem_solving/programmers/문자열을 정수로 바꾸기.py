def solution_old(s):
    return int(s) if s[0].isdigit() else -int(s[1:len(s)]) if s[0] == '-' else +int(s[1:len(s)])


def solution_new(s):
    return int(s)
