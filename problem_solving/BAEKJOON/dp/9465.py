for _ in range(int(input())):
    t = int(input())
    stickers = [[0]]

    for _ in range(2):
        stickers.append(list(map(int, input().split())))

    if t < 2:
        print(max(stickers[1][0], stickers[2][0]))
    else:
        stickers[1][1] += stickers[2][0]
        stickers[2][1] += stickers[1][0]

        for i in range(2, t):
            stickers[1][i] += max(stickers[2][i - 1], stickers[2][i - 2])
            stickers[2][i] += max(stickers[1][i - 1], stickers[1][i - 2])

        print(max(stickers[1][t - 1], stickers[2][t - 1]))
