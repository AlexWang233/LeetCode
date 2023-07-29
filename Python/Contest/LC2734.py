class Solution:
    def smallestString(self, s: str) -> str:
        res = list(s)
        start = 0
        for c in res:
            if c == 'a':
                start += 1
            else:
                break
        if start == len(s):
            res[-1] = 'z'
            return ''.join(res)
        for i in range(start, len(s)):
            if res[i] != 'a':
                res[i] = chr(ord(res[i]) - 1)
            else:
                break
        return ''.join(res)
        