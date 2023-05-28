class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] +[1]
        l = len(nums)
        dp = [[0] * l for _ in range(l)]
        for i in range(2, l):
            for left in range(l - i):
                right = left + i
                for mid in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[mid] * nums[right] + dp[left][mid] + dp[mid][right])
        return dp[0][-1]