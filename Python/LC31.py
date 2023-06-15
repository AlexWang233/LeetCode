class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        # see how many numbers are in reverse order consecutively
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # if all numbers are in reverse order, go to first permutation
        if i == 0:
            nums.reverse()
            return

        # find pivot to swap so (i-1)th index is correct
        while nums[j] <= nums[i-1]:
            j -= 1

        nums[i-1], nums[j] = nums[j], nums[i-1]

        # reverse digits after pivot
        nums[i:] = nums[len(nums)-1 : i-1 : -1]
