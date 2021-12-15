# Easy
# 383. Ransom Note

class Solution:
    def canConstruct(self, r, m):
        for c in sorted(r):
            if c not in m:
                return False
            else:
                m = m.replace(c, "*", 1)
        return True