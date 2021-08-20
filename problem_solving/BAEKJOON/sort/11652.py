from collections import Counter
from sys import stdin

cards = []

for _ in range(int(stdin.readline())):
    cards.append(int(stdin.readline()))

counted_cards = sorted(Counter(cards).most_common(), key=lambda x: (-x[1], x[0]))
print(counted_cards[0][0])
