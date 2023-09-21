class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            try:
                j = nums.index(target - x, i+1)
                return [i, j]
            except:
                pass
                