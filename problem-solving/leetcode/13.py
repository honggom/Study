class Solution:
    def romanToInt(self, s):
        sb = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0

        for i in range(len(s)):
            ans += sb[s[i]]

        for i in range(len(s) - 1):
            if sb[s[i]] < sb[s[i + 1]]:
                ans -= sb[s[i]] * 2

        return ans