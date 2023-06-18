class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]

        def dfs(i, j, prev):
            if i < 0 or j < 0:
                return 0
            if i >= n or j >= m:
                return 0
            if grid[i][j] <= prev:
                return 0
            if dp[i][j] > 0:
                return dp[i][j]
            dp[i][j] = dfs(i+1, j, grid[i][j]) + dfs(i-1, j, grid[i][j])\
                     + dfs(i, j-1, grid[i][j]) + dfs(i, j+1, grid[i][j]) + 1
            return dp[i][j]

        res = 0
        for i in range(n):
            for j in range(m):
                cur = dfs(i, j, -1)
                res += cur

        return res % (10 ** 9 + 7)

        