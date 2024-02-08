class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]

        for i in range(1, n + 1):
            m = n
            for j in range(1, math.isqrt(i) + 1):
                m = min(m, dp[- j * j] + 1)

            dp.append(m)

        return dp[-1]