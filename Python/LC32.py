class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        l = r = 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                res = max(res, l * 2)
            elif r > l:
                l = r = 0
        
        l = r = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                r += 1
            else:
                l += 1
            if l == r:
                res = max(res, r * 2)
            elif l > r:
                l = r = 0

        return res