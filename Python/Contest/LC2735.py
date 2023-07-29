class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        dp = nums.copy()
        res = sum(dp)
        l = len(nums)
        for i in range(1, l):
            for j in range(l):
                k = (i + j) % l
                dp[j] = min(dp[j], nums[k])
            res = min(res, sum(dp) + i * x)
                
        return res