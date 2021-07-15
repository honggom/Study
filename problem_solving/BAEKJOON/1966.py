T = int(input())

for _ in range(T):
    doc_count, seq = map(int, input().split())
    docs = [[False, i] for i in list(map(int, input().split()))]
    docs[seq][0] = True
    count = 0

    while True:
        max_num = max(docs, key=lambda x: x[1])[1]

        if docs[0][1] == max_num:
            count += 1
            if docs.pop(0)[0]:
                print(count)
                break
        else:
            docs.append(docs.pop(0))