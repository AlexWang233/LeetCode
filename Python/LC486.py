class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        l = len(nums)
        dp = [0] * (l + 1)
        for i in range(l):
            for j in range(i, -1, -1):
                # here dp[j] represents max net value of player 1 if we use only indices j to i
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j+1])
        return dp[0] >= 0