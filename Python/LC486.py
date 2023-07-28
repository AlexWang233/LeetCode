class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0:
            return True
        l = len(nums)
        dp = [0] * l
        for i in range(l):
            for j in range(i, -1, -1):
                if i == j:
                    dp[i] = nums[j]
                else:
                    dp[j] = max(nums[i] - dp[j], nums[j] - dp[j+1])
        return dp[0] >= 0