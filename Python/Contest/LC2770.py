class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = [0] + [-1] * (l - 1)
        for i in range(l):
            if dp[i] == -1:
                continue
            for j in range(i+1, l):
                if abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[-1]