class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        q = []
        for i in range(len(s)):
            if s[i] == '(':
                q.append(i)
            elif s[i] == ')':
                if len(q) == 0:
                    s[i] = ''
                else:
                    q.pop()

        for i in q:
            s[i] = ''

        return ''.join(s)