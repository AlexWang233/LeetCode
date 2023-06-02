class Solution:
    def maxScore(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            for j in range(i + 1, l):
                dp[i][j] = math.gcd(nums[i], nums[j])

        @lru_cache(None)
        def dfs(i, mask):
            if i > l // 2:
                return 0
            ans = 0
            for j in range(l):
                for k in range(j + 1, l):
                    cur = (1 << j) + (1 << k)
                    if not cur & mask:
                        ans = max(ans, i * dp[j][k] + dfs(i + 1, mask + cur))
            return ans

        return dfs(1, 0)

