from collections import Counter
import math

counted = Counter(input())
counted["6"] = counted["9"] = math.ceil((counted["6"] + counted["9"]) / 2)

print(counted.most_common(1)[0][1])