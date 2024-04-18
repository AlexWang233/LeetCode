class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        visited = [[False] * c for _ in range(r)]
        def dfs(i, j):
            if visited[i][j]:
                return 0
            visited[i][j] = True
            ans = 4
            if i > 0 and grid[i - 1][j]:
                ans -= 1
                ans += dfs(i - 1, j)
            if i < r - 1 and grid[i + 1][j]:
                ans -= 1
                ans += dfs(i + 1, j)
            if j > 0 and grid[i][j - 1]:
                ans -= 1
                ans += dfs(i, j - 1)
            if j < c - 1 and grid[i][j + 1]:
                ans -= 1
                ans += dfs(i, j + 1)
            return ans
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    return dfs(i, j)
        return -1
            