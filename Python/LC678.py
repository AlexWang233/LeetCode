class Solution:
    def checkValidString(self, s: str) -> bool:
        l = star = 0
        for c in s:
            if c == '(':
                l += 1
            elif c == '*':
                star += 1
            else:
                if l > 0:
                    l -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False
        r = star = 0
        for c in s[::-1]:
            if c == ')':
                r += 1
            elif c == '*':
                star += 1
            else:
                if r > 0:
                    r -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False
        return True