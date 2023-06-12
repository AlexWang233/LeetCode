class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def sink(r: int, c: int) -> None:
            if m > r >= 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 0
                for i, j in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
                    sink(i, j)

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if r in (0, m - 1) or c in (0, n - 1):
                    sink(r, c)
                    
        return sum(map(sum, grid))