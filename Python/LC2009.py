class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        nums = sorted(list(set(nums)))
        left = 0
        res = 0
        for i, n in enumerate(nums):
            if n - nums[left] >= l:
                left += 1
            else:
                res += 1

        return l - res