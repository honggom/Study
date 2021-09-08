string = input()
alpha = {}
for a in range(97, 123):
    alpha[chr(a)] = 0

for s in string:
    alpha[s] += 1

print(*alpha.values())
