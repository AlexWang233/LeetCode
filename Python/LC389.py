class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        for key in c2 - c1:
            return key
        