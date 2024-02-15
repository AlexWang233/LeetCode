class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        for i in range(1, l):
            nums[i] += nums[i - 1]
        for i in range(l - 1, 1, -1):
            if nums[i] < nums[i-1] * 2:
                return nums[i]

        return -1