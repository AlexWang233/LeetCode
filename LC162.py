class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        l = len(nums)

        if nums[-1] > nums[-2]:
            return l - 1

        left, right = 0, l - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] <= nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1

        return -1