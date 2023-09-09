class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for n in nums:
                if i < n:
                    continue
                else:
                    dp[i] += dp[i - n]
        return dp[-1]
