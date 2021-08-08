from sys import stdin

t = int(stdin.readline())
members = []
ranks = []
for _ in range(t):
    member = list(map(int, stdin.readline().split()))
    members.append(member)

for pivot_member in members:
    rank = 1
    for member in members:
        if pivot_member is not member:
            if member[0] > pivot_member[0] and member[1] > pivot_member[1]:
                rank += 1
    ranks.append(rank)

print(*ranks)

