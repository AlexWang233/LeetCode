class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h1 = h2 = -10**6
        s1 = s2 = 0
        for p in prices:
            s2 = max(s2, h2+p)
            h2 = max(h2, s1-p)
            s1 = max(s1, h1+p)
            h1 = max(h1, 0-p)
        return s2