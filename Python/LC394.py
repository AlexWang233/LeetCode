class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        n = 0
        ans = ''
        for c in s:
            if c == '[':
                stk.append(n)
                stk.append(ans)
                ans = ''
                n = 0
            elif c == ']':
                ss = stk.pop()
                m = stk.pop()
                ans = ss + ans * m
            elif c.isdigit():
                n = n * 10 + int(c)
            else:
                ans += c
        return ans
