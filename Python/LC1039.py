class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        c = 500000000
        n = len(values)
        dp = [[c] * n for _ in range(n)]

        def helper(start: int, end: int) -> int:
            if end - start <= 1:
                return 0
            if dp[start][end] < c:
                return dp[start][end]
            if end - start == 2:
                dp[start][end] = math.prod(values[start:end + 1])
                return dp[start][end]
            res = c
            for k in range(start + 1, end):
                cur = values[start] * values[k] * values[end]
                cur += helper(start, k) + helper(k, end)
                res = min(res, cur)
            dp[start][end] = res
            return res

        ans = helper(0, n - 1)
        return ans