class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def dfs(x, y, c):
            if not (0 <= x < m and 0 <= y < n):
                return 1
            if c <= 0:
                return 0
            ans = 0
            moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            for dx, dy in moves:
                ans += dfs(x + dx, y + dy,  c - 1)
            return ans
        
        mod = 10 ** 9 + 7
        res = dfs(startRow, startColumn) % mod
        return res
