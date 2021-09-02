import sys
input = sys.stdin.readline
given_puzzle = [list(input().split()) for _ in range(3)]
goal = '123456780'
history = []

def normalize(puzzle):
    normalized_puzzle = ""
    for p in puzzle:
        normalized_puzzle += "".join(p)
    return normalized_puzzle

def search(puzzle, count):
    normalized_puzzle = normalize(puzzle)
    if normalized_puzzle == goal:
        print(count)
        sys.exit(0)
    if normalized_puzzle in history:
        return
    history.append(normalized_puzzle)
    try:
        for i in range(3):
            for j in range(3):
                if puzzle[i][j] == "0":
                    # 위 puzzle[i - 1][j], puzzle[i][j] = puzzle[i][j], puzzle[i - 1][j]
                    # 아래
                    # 왼쪽
                    # 오른쪽
                    search()
                    search()
                    search()
                    search()
    except:
        print("can't go")

