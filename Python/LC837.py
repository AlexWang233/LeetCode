class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts:
            return 1
        dp = [1.0] + [0.0] * n
        m = 1.0
        res = 0
        for i in range(1, n + 1):
            dp[i] = m / maxPts
            if i < k:
                m += dp[i]
            else:
                res += dp[i]
            if i >= maxPts:
                m -= dp[i -  maxPts]
        return res