class Solution:
    def isPalindrome(self, x: int) -> bool:
        if "".join(reversed(str(x))) == str(x):
            return True
        return False