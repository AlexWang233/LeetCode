class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        h = [-2000] * k
        s = [0] * k
        for p in prices:
            for j in range(k-1, 0, -1):
                s[j] = max(s[j], h[j]+p)
                h[j] = max(h[j], s[j-1]-p)
            s[0] = max(s[0], h[0]+p)
            h[0] = max(h[0], -p)
        return s[-1]