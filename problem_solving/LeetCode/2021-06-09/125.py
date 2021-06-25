class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        for char in s:
            if char.isalnum():
                tmp.append(char.lower())

        while len(tmp) > 1:
            if tmp.pop(0) != tmp.pop():
                return False
        return True
