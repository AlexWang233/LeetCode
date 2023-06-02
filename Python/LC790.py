class Solution:
    def numTilings(self, n: int) -> int:
        m = 10**9 + 7
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        for i in range(3, n+1):
            dp.append(2*dp[i-1] + dp[i-3])
        return dp[-1] % m