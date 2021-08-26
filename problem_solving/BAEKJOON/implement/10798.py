from collections import deque
from sys import stdin

strs = [deque(list(stdin.readline().strip())) for _ in range(5)]
count, mx = 0, 0
for i in range(5):
    mx += len(strs[i])
pointer = 0

while count != mx:
    if len(strs[pointer]) > 0:
        print(strs[pointer].popleft(), end="")
        count += 1
    pointer += 1
    if pointer > 4:
        pointer = 0