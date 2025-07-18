class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        dp = [[0] * k for _ in range(k)]
        ans = 0
        
        for n in nums:
            i = n % k
            for j in range(k):
                dp[j][i] = dp[i][j] + 1
                ans = max(ans, dp[j][i])
        
        return ans