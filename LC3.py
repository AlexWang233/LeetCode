from queue import Queue

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = m = 0
        d = {}
        
        for i, c in enumerate(s):
            if c in d and d[c] >= start:
                start = d[c] + 1
            else:
                m = max(m, i - start + 1)
            d[c] = i
        return m