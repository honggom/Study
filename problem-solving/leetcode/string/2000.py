# Easy
# 2000. Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word, ch):
        try:
            index = word.index(ch)
        except:
            return word
        return "".join(list(reversed(word[0:index + 1]))) + word[index + 1:]