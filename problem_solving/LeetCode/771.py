from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = Counter(stones)
        c = 0
        for key in s.keys():
            if key in jewels:
                c += s[key]
        return c