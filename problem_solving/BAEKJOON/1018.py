# # 체스판 다시 칠하기 문제
# #
# # 1. 우선 나눠질 수 있는 모든 체스판을 알아야 될 것 같다.
# # 8, 8이면 나눠질 수 없다.
#
# from sys import stdin
#
# # n : 행의 수, m : 열의 수
# n, m = map(int, stdin.readline().split())
#
# given_board = []
#
# for i in range(n):
#     given_board.append(stdin.readline().rstrip())
#
#
# def make_new_board(start, given_board):
#     new_board = []
#     cur_color = 'W' if start == 'B' else 'B'
#     for i in range(len(given_board)):
#         row = list(given_board[i])
#         new_row = []
#         for j in range(len(row)):
#             if i == 0 and j == 0:
#                 new_row.append([start, start != row[j]])
#             elif j == len(row) - 1 and m % 2 == 0:
#                 new_row.append([cur_color, cur_color != row[j]])
#                 cur_color = 'B' if cur_color == 'B' else 'W'
#             else:
#                 cur_color = 'W' if cur_color == 'B' else 'B'
#                 new_row.append([cur_color, cur_color != row[j]])
#         new_board.append(new_row)
#     return new_board
#
# start_black_board = make_new_board('B', given_board)
# start_white_board = make_new_board('W', given_board)
#
# def separate_board(board):
#     if len(board) == 8 and len(board[0]) == 8:
#         print("88")
#
#     # separated_boards = []
#
#
# # if n == 8 and m == 8:
# #     print("88")
# # else:
# #     separated_boards = []
# #     #while True:
# #     for row in start_black_board:
# #         for index in range(len(row)):
# #             if
# for aa in start_black_board:
#     print(aa)
# print(len(start_black_board))
# print(len(start_black_board[0]))


n, m = map(int, input().split())
given_board = []
counts = []

for _ in range(n):
    given_board.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1, idx2 = 0, 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):                # 8X8 범위를 B와 W로 번갈아가면서 검사
                if (j + b) % 2 == 0:
                    if given_board[b][j] != 'W': idx1 += 1
                    if given_board[b][j] != 'B': idx2 += 1
                else :
                    if given_board[b][j] != 'B': idx1 += 1
                    if given_board[b][j] != 'W': idx2 += 1
        counts.append(idx1)                          # W로 시작했을 때 칠해야 할 부분
        counts.append(idx2)                          # B로 시작했을 때 칠해야 할 부분

print(min(counts))
