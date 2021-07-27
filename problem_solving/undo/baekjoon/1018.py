# 체스판 다시 칠하기 문제
#
# 1. 우선 나눠질 수 있는 모든 체스판을 알아야 될 것 같다.
# 8, 8이면 나눠질 수 없다.

from sys import stdin

# n : 행의 수, m : 열의 수
n, m = map(int, stdin.readline().split())

given_board = []

for i in range(n):
    given_board.append(stdin.readline().rstrip())


def make_new_board(start, given_board):
    new_board = []
    cur_color = 'W' if start == 'B' else 'B'
    for i in range(len(given_board)):
        row = list(given_board[i])
        new_row = []
        for j in range(len(row)):
            if i == 0 and j == 0:
                new_row.append([start, start != row[j]])
            else:
                new_row.append([cur_color, cur_color != row[j]])
                cur_color = 'W' if cur_color == 'B' else 'B'
            if j == len(row) - 1:
                cur_color = 'W' if cur_color == 'B' else 'B'
        new_board.append(new_row)

    return new_board

b = make_new_board('B', given_board)
w = make_new_board('W', given_board)

for bs in b:
    print(bs)

print("-----------------")
print("-----------------")
print("-----------------")

for ws in w:
    print(ws)






