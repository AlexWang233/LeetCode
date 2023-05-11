class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rs, ls = sum(nums[1:]), 0
        i = 0
        while i < len(nums):
            if rs ==  ls:
                return i
            ls += nums[i]
            i+=1
            if i < len(nums):
                rs -= nums[i]
        return -1        