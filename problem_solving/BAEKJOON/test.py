fruitWeights = [30, 40, 10, 20, 30]
k = 3

def solution(fruitWeights, k):
    n = 0
    result = set()
    max_len = len(fruitWeights) + 1

    while True:
        result.add(max(fruitWeights[n:k]))
        n += 1
        k += 1
        if k == max_len:
            break

    return sorted(result, reverse=True)

print(solution(fruitWeights, k))