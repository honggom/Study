# Easy
# 1859. Sorting the Sentence

class Solution:
    def sortSentence(self, s):
        strs = s.split()
        result = [''] * len(strs)

        for st in strs:
            result[int(st[-1]) - 1] = st[:-1]

        return " ".join(result)