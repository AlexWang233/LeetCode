class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = suffix = 1
        for i, n in enumerate(nums):
            ans[i] *= prefix
            ans[~i] *= suffix
            prefix *= n
            suffix *= nums[~i]
        return ans