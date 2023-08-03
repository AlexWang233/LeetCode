class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [1] + [0] * n
        p = 1
        mod = 10 ** 9 + 7
        while (m := pow(p, x)) <= n:
            for i in range(n, m-1, -1):
                dp[i] += dp[i-m]
                dp[i] %= mod
            p += 1
        return dp[-1]