class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        dp = [True] + [False] * l
        dp[2] = (nums[0] == nums[1])
        for i in range(2, l):
            if dp[i - 1]:
                if nums[i] == nums[i-1]:
                    dp[i + 1] = True
                    continue
            if dp[i - 2]:
                if nums[i] == nums[i-1] == nums[i-2]:
                    dp[i + 1] = True
                elif (nums[i] - 1) == nums[i-1] == (nums[i-2] + 1):
                    dp[i + 1] = True
        return dp[-1]
