class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        @functools.lru_cache(None)
        def dp(i, k):
            if i == -1 or k == 0:
                return 0

            l = min(len(piles[i]), k)
            ans, cur = dp(i - 1, k), 0

            for j in range(l):
                cur += piles[i][j]
                ans = max(ans, dp(i - 1, k - j - 1) + cur)
            return ans

        return dp(len(piles) - 1, k)



