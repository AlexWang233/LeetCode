class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        l = len(piles)
        dp = [[0] * l for _ in range(l)]
        for i in range(l-2, -1, -1):
            piles[i] += piles[i+1]
        
        def dfs(i, m):
            n = 0
            idx = min(i + 2*m, l)
            if idx == l:
                return piles[i]
            if dp[i][m]:
                return dp[i][m]
            for j in range(i, idx):
                n = max(n, piles[i] - dfs(j+1, max(m, j - i + 1)))
            dp[i][m] = n
            return n

        return dfs(0, 1)

        
