class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0,n])
        cuts.sort()
        l = len(cuts)
        dp = [[0] * l for _ in range(l)]
        for i in range(2, l):
            for j in range(l - i):
                for k in range(1, i):
                    if dp[j][j + i] == 0:
                        dp[j][j+i] = cuts[j+i] - cuts[j] + dp[j][j+k] + dp[j+k][j+i]
                        continue
                    dp[j][j+i] = min(dp[j][j+i], cuts[j+i] - cuts[j] + dp[j][j+k] + dp[j+k][j+i])
        return dp[0][-1]