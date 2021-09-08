from sys import stdin

members = []

for _ in range(int(stdin.readline())):
    members.append(list(stdin.readline().split()))

[print(member[0]) for member in sorted(members, key=lambda m: (-int(m[1]), int(m[2]), -int(m[3]), m[0]))]