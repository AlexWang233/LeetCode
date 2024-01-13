class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        for c in c1.copy().keys():
            c1[c] = c1[c] - c2[c]
            if c1[c] < 0:
                del c1[c]
        return sum(c1.values())
        
