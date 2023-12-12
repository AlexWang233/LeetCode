class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur = nums[0] - 1
        res = 0
        for i in range(1, len(nums)):
            res = max(res, cur * (nums[i] - 1))
            if nums[i] > cur:
                cur = nums[i] - 1

        return res