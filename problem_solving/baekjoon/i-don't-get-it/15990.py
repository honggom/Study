sequences, sequence = [], []
n = int(input())


def dfs(index):
    if len(sequence) > 1 and sequence[-1] == sequence[-2]:
        return
    if sum(sequence) == n:
        sequences.append(sequence[:])
        return
    else:
        for i in range(index, 4):
            sequence.append(i)
            dfs(1)
            sequence.pop()

dfs(1)
print(sequences)

