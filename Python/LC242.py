from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = defaultdict(lambda: 0)
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        return all(val == 0 for val in d.values())