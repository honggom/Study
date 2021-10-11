from itertools import combinations

common = ["a", "t", "n", "i", "c"]
n, k = map(int, input().split())

strs = []

if k < 6:
    print(0)
else:
    for _ in range(n):
        strs.append("".join(set(input()[4:-4])))

    tmp = []
    init = 0

    for i in range(len(strs)):
        tmp_str = strs[i]
        for st in strs[i]:
            if st in common:
                tmp_str = tmp_str.replace(st, "")
        if tmp_str != "":
            tmp.append(tmp_str)
        else:
            init += 1

    old_length = len(tmp)
    new_length = 0
    count = k - 5
    alphas = set([s for st in tmp for s in st])

    for comb in combinations(alphas, count):
        temp = []
        for st in tmp:
            temp_str = st
            for c in comb:
                temp_str = temp_str.replace(c, "")

            if temp_str != "":
                temp.append(temp_str)

        new_length = max(new_length, old_length - len(temp))

    print(new_length + init)