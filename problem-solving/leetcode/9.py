class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if "".join(reversed(str(x))) == str(x):
            return True
        return False