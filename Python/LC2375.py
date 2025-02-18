class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = ""
        stk = []

        for i in range(n + 1):
            stk.append(i + 1)
            if i == n or pattern[i] == 'I':
                while stk:
                    res += str(stk.pop())
                    
        return res