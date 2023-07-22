class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = defaultdict(lambda: -1)
        directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        def helper(k, r, c):
            if r < 0 or c < 0 or r >= n or c >= n:
                return 0
            if k == 0:
                return 1
            if (r, c, k) in dp:
                return dp[(r, c, k)]
            ans = 0
            for x, y in directions:
                ans += helper(k - 1, r + x, c + y)

            ans /= 8
            dp[(r, c, k)] = ans
            dp[(n - r - 1, c, k)] = ans
            dp[(r, n - c - 1, k)] = ans
            dp[(n - r - 1, n - c - 1, k)] = ans
            return ans
        
        res = helper(k, row, column)
        return res

            