class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        nums = sorted(envelopes, key = lambda x: [x[0], -x[1]])  
        dp = [10**5+1] * (len(nums) + 1)
        for elem in nums: dp[bisect_left(dp, elem[1])] = elem[1]  
        return dp.index(10**5+1)
        