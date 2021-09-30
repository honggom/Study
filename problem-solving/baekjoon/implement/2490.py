from collections import Counter

cases = [list(map(int, input().split())) for _ in range(3)]

for case in cases:
    counted_case = Counter(case)
    if counted_case[0] == 1:
        print("A")
    elif counted_case[0] == 2:
        print("B")
    elif counted_case[0] == 3:
        print("C")
    elif counted_case[0] == 4:
        print("D")
    else:
        print("E")

