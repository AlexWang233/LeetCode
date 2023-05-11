class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for nz in range(len(nums)):
            if nums[nz]:
                nums[z], nums[nz] = nums[nz], nums[z]
                z += 1