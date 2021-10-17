def solution(s):
    ans = len(s)

    if len(s) == 1:
        return 1
    for cut in range(1, (len(s) // 2) + 1):
        string = ""
        count = 1
        cur = s[:cut]

        for i in range(cut, len(s), cut):
            if cur == s[i:cut+i]:
                count += 1
            else:
                if count == 1:
                    string += cur
                else:
                    string += str(count) + cur
                cur = s[i:cut+i]
                count = 1

        if count == 1:
            string += cur
        else:
            string += str(count) + cur

        ans = min(ans, len(string))

    return ans