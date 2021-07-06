t = int(input())
members = []
for i in range(t):
    tmp = input().split()
    tmp.append(i)
    members.append(tmp)

members.sort(key=lambda x: (int(x[0]), x[2]))

for member in members:
    print(member[0], member[1])