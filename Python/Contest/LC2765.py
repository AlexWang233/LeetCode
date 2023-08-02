class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        res = prev = -1
        for i in range(1, l):
            if prev > 0 and nums[i] == nums[i-2]:
                prev += 1
            else:
                if nums[i] == nums[i-1] + 1:
                    prev = 2
                else:
                    prev = -1
            res = max(res, prev)
        return res