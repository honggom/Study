class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        import re
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]
        from collections import Counter

        return Counter(words).most_common()[0][0]
