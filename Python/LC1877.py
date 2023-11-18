class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums) // 2
        res = 0
        for i in range(l):
            res = max(res, nums[i] + nums[~i])
        return res