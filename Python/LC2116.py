class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        l = len(s)
        if l % 2 != 0:
            return False

        open = 0
        for i in range(l):
            if s[i] == '(' or locked[i] == '0':
                open += 1
            else:
                open -= 1
            if open < 0:
                return False

        closed = 0
        for i in range(l - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                closed += 1
            else:
                closed -= 1
            if closed < 0:
                return False
        return True