n = int(input())

for _ in range(n):
    quiz = list(input())
    total = 0
    score = 1
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            total += score
            score += 1
        else:
            score = 1
    print(total)
