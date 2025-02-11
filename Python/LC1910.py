class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = s.find(part)
        while(i > -1):
            s = s[:i] + s[i + len(part):]
            i = s.find(part)
        return s