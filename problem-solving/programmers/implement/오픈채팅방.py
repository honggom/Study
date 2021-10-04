def solution(record):
    temp = []
    names = {}
    result = []

    for r in record:
        cmd = r.split()

        if cmd[0] == "Enter":
            temp.append([cmd[1], '님이 들어왔습니다.'])
            names[cmd[1]] = cmd[2]
        elif cmd[0] == "Leave":
            temp.append([cmd[1], '님이 나갔습니다.'])
        else:
            names[cmd[1]] = cmd[2]

    for t in temp:
        result.append(names[t[0]] + t[1])

    return result