class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n, m = len(grid), len(grid[0])
        ans = 0

        def dfs(r, c):
            nonlocal n, m
            res = 0
            if grid[r][c] == 0:
                return res
            
            res += grid[r][c]
            grid[r][c] = -1

            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[nr][nc] > 0:
                        res += dfs(nr, nc)

            return res

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                ans = max(ans, dfs(i, j))
        
        return ans
