class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        t = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c not in t.values():
                if len(stack) == 0:
                    return False
                if stack.pop() != t[c]:
                    return False
            else:
                stack.append(c)

        return False if len(stack) != 0 else True