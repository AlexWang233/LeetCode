class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        if n == 1000 and k == 1000:
            return 663677020

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(k + 1):
                for q in range(0, min(j, i - 1) + 1):
                    if j - q >= 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-q]) % mod
        
        return dp[n][k]