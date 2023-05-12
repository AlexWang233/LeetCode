class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        dp = [0] * (l + 1)
        for c in citations:
            dp[min(c, l)] += 1
        ans = 0
        for i in range(l, -1, -1):
            ans += dp[i]
            if ans >= i:
                return i
        return ans