class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for n in nums:
            if j == 0 or n > nums[j-1]:
                nums[j] = n
                j += 1
        return j