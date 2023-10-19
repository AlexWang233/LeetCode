class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p = q = ""
        for i in s:
            if i != '#':
                p += i
            else:
                p = p[:-1] if len(p) > 0 else ""

        for i in t:
            if i != '#':
                q += i
            else:
                q = q[:-1] if len(q) > 0 else ""

        return p == q