class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl, ml = len(needle), len(haystack)
        if nl == 0:
            return nl
        if ml < nl:
            return -1
        for i in range(ml - nl + 1):
            if haystack[i:i+nl] == needle:
                return i
        return -1