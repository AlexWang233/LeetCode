class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            dp[i] = max([dp[j] * (i - j) for j in range(1, i)] + [j * (i - j) for j in range(1, i//2 + 1)])
        return dp[-1]